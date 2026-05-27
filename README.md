# ABC Behavior Parser

ABC Behavior Parser is an educational prototype that helps caregivers convert plain-language child behavior notes into a simple ABC structure: Antecedent, Behavior, and Consequence.

A simple educational prototype that helps caregivers organize child behavior observations into ABC format.

## Example

Input:

"My child got upset when screen time ended and threw the toy."

Output:

- Antecedent: Screen time ended
- Behavior: Got upset and threw the toy
- Consequence: Not clearly mentioned
- Possible trigger: Transition from preferred activity
- Suggested follow-up question: What happened immediately after the toy was thrown?

## Purpose

Many parents and caregivers observe behavior every day but may not know how to organize those notes for therapy, school, or professional discussions. This project provides a simple structure for organizing observations.

## Planned Features

- Plain-language behavior note input
- ABC structure extraction
- Possible trigger identification
- Suggested caregiver follow-up questions
- Sample synthetic behavior notes
- Simple demo app

## Not Intended For

- Diagnosis
- Treatment recommendation
- Clinical decision-making
- Replacing therapists, teachers, or clinicians

## Disclaimer

This project is for educational and caregiver-support purposes only. It is not medical advice, diagnosis, or treatment.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the demo app:

```bash
streamlit run app.py
```

The app should open in your browser at:

```text
http://localhost:8501
```

## Sample Inputs

Try these examples:

```text
My child got upset when screen time ended and threw the toy.

My child cried after being asked to start homework.

My child covered ears in the grocery store when the noise became loud.
```
