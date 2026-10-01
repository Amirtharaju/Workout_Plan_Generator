import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq


# ============================================================
# Configuration
# ============================================================

load_dotenv()

st.set_page_config(
    page_title="Workout Plan Generator",
    page_icon="💪",
    layout="wide",
)


# ============================================================
# Validation
# ============================================================

def validate_inputs(
    goal: str,
    experience: str,
    days: int,
    equipment: str,
) -> str | None:
    """
    Validate the user's workout inputs.

    Returns:
        None if inputs are valid.
        Error message if inputs are invalid.
    """

    if not goal:
        return "Please select a fitness goal."

    if not experience:
        return "Please select your experience level."

    if days < 1 or days > 7:
        return "Days available must be between 1 and 7."

    if not equipment:
        return "Please select your equipment access."

    return None


# ============================================================
# Prompt Builder
# ============================================================

def build_workout_prompt(
    goal: str,
    experience: str,
    days: int,
    equipment: str,
    limitations: str,
) -> str:
    """
    Build the prompt that will be sent to the LLM.
    """

    prompt = f"""
You are an experienced personal fitness programming assistant.

Create a practical weekly workout plan based on the following
user profile.

USER PROFILE
------------

Fitness goal:
{goal}

Experience level:
{experience}

Days available:
{days}

Equipment available:
{equipment}

Limitations:
{limitations if limitations else "None reported"}


REQUIREMENTS
------------

1. Create exactly {days} workout days.
2. Respect the user's fitness goal.
3. Respect the user's experience level.
4. ONLY use equipment available to the user.
5. Do not recommend equipment that the user does not have.
6. Respect the user's stated limitations.
7. If the user has provided an injury, pain, or physical limitation:
   - Avoid exercises that obviously conflict with the limitation.
   - Do not diagnose the condition.
   - Do not claim that an exercise is medically safe.
   - Prefer conservative exercise choices.
   - Include a short disclaimer recommending consultation
     with an appropriately qualified healthcare professional
     when appropriate.
8. Make the plan realistic for the number of available days.
9. Include recovery/rest days when appropriate.
10. Do not make medical diagnoses or medical claims.
11. Keep the plan appropriate for the user's experience level.
12. The workout should be practical enough for a real person
    to follow.

OUTPUT FORMAT
-------------

Return the answer using Markdown.
Start with:

# Weekly Workout Plan

Then include:

## Plan Overview

Include:

- Goal
- Experience
- Training days
- Equipment

Then provide a section for every workout day.

For example:

## Day 1 - Workout Focus

Use this table:

| Exercise | Sets | Reps/Duration | Rest |
|----------|------|---------------|------|
| Exercise 1 | 3 | 8-12 | 60 sec |
| Exercise 2 | 3 | 10-12 | 60 sec |

Repeat the same structure for every workout day.

Create exactly {days} workout days.

Finally include:

## Weekly Schedule

Clearly show workout days and recovery/rest days.

Then include:

## Progression Tips

Provide 3-5 practical progression tips.

The final answer must be specific and actionable,
not generic fitness advice.

IMPORTANT:

Do not ignore the user's equipment,
experience level, number of available days,
or limitations.
"""


    return prompt


# ============================================================
# Groq Client
# ============================================================

def get_groq_client() -> Groq:
    """
    Create and return a Groq client.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please check your .env file."
        )

    return Groq(api_key=api_key)

        
# ============================================================
# Generate Workout Plan
# ============================================================

def generate_workout_plan(
    goal: str,
    experience: str,
    days: int,
    equipment: str,
    limitations: str,
) -> str:
    """
    Generate a personalized workout plan using Groq.
    """

    # --------------------------------------------------------
    # Step 1: Validate inputs
    # --------------------------------------------------------

    error = validate_inputs(
        goal,
        experience,
        days,
        equipment,
    )

    if error:
        raise ValueError(error)


    # --------------------------------------------------------
    # Step 2: Build prompt
    # --------------------------------------------------------

    prompt = build_workout_prompt(
        goal,
        experience,
        days,
        equipment,
        limitations,
    )


    # --------------------------------------------------------
    # Step 3: Call Groq
    # --------------------------------------------------------

    try:

        client = get_groq_client()

        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a precise fitness programming "
                        "assistant. Follow the user's constraints "
                        "exactly."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.5,
            max_completion_tokens=4000,
        )


        # ----------------------------------------------------
        # Step 4: Validate response
        # ----------------------------------------------------

        if not response.choices:
            raise ValueError(
                "The LLM returned no response."
            )


        # ----------------------------------------------------
        # Step 5: Extract response text
        # ----------------------------------------------------

        content = response.choices[0].message.content


        # ----------------------------------------------------
        # Step 6: Check for empty response
        # ----------------------------------------------------

        if not content or not content.strip():
            raise ValueError(
                "The LLM returned an empty response."
            )


        # ----------------------------------------------------
        # Step 7: Return workout plan
        # ----------------------------------------------------

        return content.strip()


    except ValueError:
        raise


    except Exception as exc:

        raise RuntimeError(
            f"Unable to generate workout plan: {exc}"
        ) from exc


# ============================================================
# Streamlit UI
# ============================================================

st.title("💪 Workout Plan Generator")

st.write(
    "Tell us about yourself and generate a personalized "
    "weekly workout plan."
)

st.divider()

st.subheader("👤 Tell us about yourself")


# ============================================================
# User Inputs
# ============================================================

col1, col2 = st.columns(2)


with col1:

    goal = st.selectbox(
        "Fitness Goal",
        [
            "Build muscle",
            "Lose fat",
            "General fitness",
            "Improve endurance",
        ],
    )


    experience = st.selectbox(
        "Experience Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )


    days = st.slider(
        "Days Available Per Week",
        min_value=1,
        max_value=7,
        value=3,
    )


with col2:

    equipment = st.selectbox(
        "Equipment Access",
        [
            "No equipment",
            "Home dumbbells",
            "Full gym",
        ],
    )


    limitations = st.text_area(
        "Injuries or Limitations (Optional)",
        placeholder=(
            "Example: bad knees, no overhead pressing..."
        ),
        height=120,
    )


# ============================================================
# Display Selected Inputs
# ============================================================

st.divider()

st.subheader("📋 Your Selections")

summary_col1, summary_col2, summary_col3, summary_col4 = (
    st.columns(4)
)


with summary_col1:

    st.write("**Goal**")

    st.write(goal)


with summary_col2:

    st.write("**Experience**")

    st.write(experience)


with summary_col3:

    st.write("**Training Days**")

    st.write(days)


with summary_col4:

    st.write("**Equipment**")

    st.write(equipment)


# ============================================================
# Generate Button
# ============================================================

st.divider()

generate = st.button(
    "🚀 Generate Workout Plan",
    type="primary",
    use_container_width=True,
)


if generate:

    # --------------------------------------------------------
    # Validate inputs
    # --------------------------------------------------------

    error = validate_inputs(
        goal,
        experience,
        days,
        equipment,
    )


    if error:

        st.warning(error)


    else:

        # ----------------------------------------------------
        # Generate workout
        # ----------------------------------------------------

        with st.spinner(
            "Creating your personalized workout plan..."
        ):

            try:

                plan = generate_workout_plan(
                    goal,
                    experience,
                    days,
                    equipment,
                    limitations,
                )


                # --------------------------------------------
                # Display result
                # --------------------------------------------

                st.success(
                    "Workout plan generated successfully!"
                )

                st.divider()

                st.subheader(
                    "🏋️ Your Personalized Workout Plan"
                )

                st.markdown(plan)


            except ValueError as exc:

                st.warning(str(exc))


            except RuntimeError as exc:

                st.error(str(exc))


            except Exception as exc:

                st.error(
                    f"Something went wrong: {exc}"
                )
