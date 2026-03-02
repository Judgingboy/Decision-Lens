# Research Log

## Overview

| Section | Navigation |
| :--- | :--- |
| **Philosophical Foundation** | [References That Influenced My Approach](#references-that-influenced-my-approach) |
| **AI Integration Policy** | [AI Usage Policy](#ai-usage-policy) |
| **AI Prompts** | [Prompts Used](#prompts-used) |
| **External Research** | [Search Queries](#search-queries) |
| **Academic & Technical Links** | [References](#references) |
| **Design Evolution** | [Accepted vs Rejected Ideas](#accepted-vs-rejected-ideas) |

### References That Influenced My Approach
This project was shaped by recurring patterns observed across decision theory, explainable systems, and practical product design rather than a single academic source.

#### 1. Decision Theory & Scoring Models
- **Weighted Sum Model (WSM):** A standard approach for multi-criteria decision-making. Influenced the core logic: weighted normalization → aggregation → ranking.
- **MCDA Concepts:** Reinforced the importance of explicit trade-offs and prioritizing explainability over black-box optimization.

#### 2. Explainable Systems & Trust
- **XAI Principles:** Users trust systems they can audit. Explanations must align perfectly with underlying logic.
- **Design Impact:** Motivated deterministic scoring and a strict separation between mathematical computation and narration.

#### 3. Practical Product Documentation
- **Transparency-First Docs:** Influenced the problem-to-solution framing and the explicit documentation of design trade-offs.
- **Architectural Clarity:** Prioritized transparency over marketing-style abstraction.

#### 4. Human Factors & UX Observations
- **Behavioral Insights:** Users struggle with abstract scoring (1–10) and prefer stating facts over doing math.
- **Result:** Shifted normalization and scale mapping from the user to the engine.

---

### AI Usage Policy
AI was utilized as an assistive layer, strictly adhering to a "Suggestive, Not Authoritative" role.

| Category | AI Role & Implementation |
| :--- | :--- |
| **Accepted** | Used for **structuring and narration only**. The Structure Agent converts free-form user input into a draft set of options, criteria, and attribute descriptions. The Explanation Agent converts deterministic engine outputs into human-readable explanations without altering scores or rankings. |
| **Modified** | AI-generated drafts are treated as **suggestions, not truth**. Users must explicitly confirm or edit cost vs. benefit classification, ordinal scales, and extracted criteria. Any AI-proposed structure can be overridden before it enters the decision engine. |
| **Rejected** | AI is **never allowed** to assign weights, normalize values, compute scores, rank options, or influence final outcomes. All mathematical operations are handled exclusively by deterministic code to ensure repeatability, auditability, and trust. |

**Key Principle:** AI is used to reduce user friction, not to replace human judgment.

### AI Prompting Notes

During development, multiple iterative prompts were used to:
- Extract draft decision structures from natural language
- Test failure modes in cost vs benefit classification
- Validate explanation consistency
- debug and enhance the code


These prompts were exploratory and iterative by nature.  
They are not included inline to preserve clarity, can be found below:

## AI Usage

### Prompts Used
- "What is a Decision Companion System?"

- "What would be a real life example?"
- "How to responsibly integrate LLMs into decision systems?"
- "At the core what do they mean by a decision companion system?"
- "What would be a real life example of a decision companion system?"
- "Are they referring to a chatbot with inputs and constraints?"
- "Are LLMs required for this assignment?"
- "How is it possible to build this without AI?"
- "If AI is used, how should it be justified and limited?"
- "How to collect options and criteria dynamically from the user?"
- "How to normalize weights so that they sum to 1?"
- "How should ratings be handled in a weighted scoring system?"
- "Like i need to make this before March 2nd and i don't know how to tackle this question"
- "Okk so Are they reffering to a chat bot? with inputs and constraints given to it?"
- "I have a simple doubt for this LLM's should be used right?"
- "How the is it even possible?"
- "How to design an explainable decision-making system?"
- "Explain weighted scoring model with examples"
- "How to structure decision logic without relying on AI?"
- "Okk so this is what we're going to do: 1. Create a repo... 2. Take OpenAI API Keys..."
- "Give me some repo names"
- "Update the wording of that one AI box"
- "But i need you to make it a typed flowchart so that i can add it in Design_Diagram.md"
- "Anyways so what ive done today is made a repo designed a flow diagram and now what i need is how do i do this in a weighted approach?"
- "So essentally these are the challenges that i have right now: 1. Store variables... 2. Validation equation... 3. Make 3 agents..."
- "Okk so why are we using the def main()?"
- "yk what just give me an input to test it, a real world example of laptops in the price range 40,000-60,000"
- "Well im gonna need the ai queries and the search queries from today so that i can document it."
- "Nah what we're gonna do today is: 1. Add details in BUILD_PROCESS.md... 2. Add prompts... 3. Structure... 4. Static model... 5. API key"
- "We need to fix this Normalize cost criteria, i mean if user enters something and if its going inverted then its a problem.. should we add in AI here?"
- "i have no idea what you just said, ill tackle this tomorrow first thing in the morning as my head is spinning"
- "Some criteria are better when numbers are higher, some are better when numbers are lower."
- "I shalll upate this now get_list_from_user, Just rename all the things with the old ones so there's no comfusion"
- "Okk now give me some options to test this new change"
- "while the program is asking for this umm what should i even do?"
- "so how do i make this program understand which criteria should be which?"
- "We are going to do this: Rank criteria by importance..."
- "shoud i remove the Rate each option for each criterion (1–10):"
- "This function? i mean, i replaced the get_weights function with get_weights_from_ranking and this seems confusing as hell this rate each option"
- "This is the headache.. Ill tell you two major flaws in this... 1. Priority vs ratings... 2. Final list is wrong..."
- "We should go with model 2, WE need AI to help in this scenario"
- "Accept criteria (which may have different weights or importance)"
- "So ig using AI is useful, I cant use Langchain because for it to work API is essential but what if i use it directly on python? It would run without fully relying on AI right?"
- "decision-lens This is good"
- "<image> Well i have this as a design"
- "So essentally these are the challenges that i have right now."
- "1. I need to store the varibles for accepting multiple options.What would be the best data structure? The thing which is coming into my mind is list, as i can store the options as well as criteria and i can change it in the future as well.."
- "2.I need a vaidation equation."
- "3.I need to make 3 agents:"
- "a. The initial agent which helps the user with option and criteria. we'll call it structure agent"
- "b. Score agent which is used only if the user cannot provide ratings by themselves"
- "c. Explanation Generator which will provide the final explanation"
- "Modified the readme"
- "Nah what we're gonna do today is "
- "1. Add details in BUILD_PROCESS.md ill provide a rough sketch you'll have to polish it later."
- "2.Add the prompts as well as Google searches till today in RESEARCH_LOG.md"
- "3. I need a structure for this, i meant the architecture of what files are needed "
- "4. I need a working static model atleast so i can conclude if it works or not and then in the next iteration , it can be dynamic model "
- "5. Get an OPENAI API key "
- "“Some criteria are better when numbers are higher, some are better when numbers are lower.”"
- "Enter importance for each criterion (any positive number):"
- "Price:"
- "We are going to do this"
- "Rank criteria by importance (1 = highest):"
- "1. Price"
- "2. RAM"
- "3. Performance"
- "4. Battery"
- "right now as the UI is confusing as hell."
- "Option: Laptop A (₹42k, i3, 8GB RAM)"
- "This is the headache.. Ill tell you two major flaws in this. 1.I've already given the priority but its again asking for ratings.. No user understands how to enter rating from 1 to 10. So either get rid of that or make a workaround from the priority or we'll make ai do that for the user. That itself is confusing af. 2. The final list is absolutely wrong. it just put the priciest laptop on top"
- "How scoring works WITHOUT ratings
  You already have laptop specs embedded in option names:
  This decision system is not just for laptops its for every domain, laptop was just an example"
- "We should go with model 2, WE need AI to help in this scenario"
- "Well we're going the AI route now.. So Ive generated an API key from OPENAI suggest me what model i should go for and ive only added 10Dollars into it. so.."
- "Okk so this is the thing, What i intend to do with the AI, restructure the input from the user, If user asks for whats the best SUV i can get in the budget of 10 Lakhs with the most power, 5 seater , has a brand value. Well it should generate constraints right? and options.. Then it can ask user for priority and everything. But the Model should know what all are the cars in the market right?.. So ig the first agent would have to do a digging from the internet rigtht?"
- "Yeah youre absolutely right.. Ig it doesnt have to be that complex"
- "<pasted the valication engine> change it so that it normalises weights"
- "<pasted the decisom_engine> "
- "<pasted the get weights function> what about this function now?"
- "So we're removing get_ratings right?"
- "structure_agent → attributes We shall do this tomorrow But right now,its testing time"
- "uhh.. i dont understand what you mean nor do i know how to make this file for testing.
  tell you what This is how we're gonna test it..
  I wanna buy a laptop where the priority is Performance>Price>RAM>Battery>Material
  Suppose there are 4 laptops in this scenario "
- "<pasted the main function> I mean what changes should be done here as we've removed ratings? "
- "So..let me get this straight.. we need 3 agents right? An input agent to get inputs and structure it. Another agent for this rating generation and at last an explanation agent"
- "So.. explain to me how the code actually works because I'm not exactly sure of what's happening rn"
- "Where would I keep the api key? And how would I call it?"
- "We're going to use the .env so anyone can just add in their own api key "
- "Can I like import OPEN_API_KEY or something? For example I'll make a ".env" file and add OPEN_AI_KEY= <KEY> inside it"
- "how can I test if the Api key work.. i mean I did buy credits into the OPENAI account "
- "before that how much should i add as a limit?"
- "a virtual environment is a good idea right? so that dependencies are isolated?"
- "API key works,got this lets just ask it to tell a joke "
- "should the .vscode forlder be added into gitignore?"

## Accepted vs Rejected Ideas
Initial thoughts on system architecture:

### Idea 1
1. **Structure Agent**: Whose only job is to convert user's decision problem into structured data.
2. **Scoring Agent**: Whose job is to estimate relative scores for options against the criteria.
3. **Explanation Agent**: Whose job is to explain decision results clearly and simply.

### Idea 2
1. **Structure Agent (Input → Attributes)** ✅
   - _(AI-assisted, optional)_
   - **What it does:**
     - Takes messy human language
     - Extracts:
       - Options
       - Criteria
       - Cost vs Benefit
       - Raw attributes (numbers, categories, unknowns)

2. **Explanation Agent (Scores → Human Explanation)** 📝
   - _(Optional AI polish)_
   - **What it does:**
     - Turns math + rankings into readable explanations
     - Highlights dominant criteria and trade-offs
     - Mirrors user priorities

```python
# TEMPORARY TEST DATA (attributes, not ratings)
# Treat these as raw factual values
attributes = {
    "Laptop A": {
        "Performance": 9,
        "Price": 9,
        "RAM": 8,
        "Battery": 6,
        "Material": 8
    },
    "Laptop B": {
        "Performance": 7,
        "Price": 6,
        "RAM": 7,
        "Battery": 7,
        "Material": 7
    },
    "Laptop C": {
        "Performance": 5,
        "Price": 3,
        "RAM": 6,
        "Battery": 8,
        "Material": 6
    },
    "Laptop D": {
        "Performance": 6,
        "Price": 7,
        "RAM": 6,
        "Battery": 6,
        "Material": 9
    }
}
```

"this is the test data, and in the real world no human is gonna type like this. So does this come under structure agent?"

- "Give me the code for the structure agent"
- "how do i test this?"
- "well it did run and the structered data is spat out"

```text
Describe your decision problem:
Type 'done' on a new line when finished.
> I want to buy a phone.
> Battery life matters more than price.
> Phone A is cheap but average battery.
> Phone B is expensive but excellent battery.
> done

Identified options:
1. Phone A
2. Phone B
[a] Add option  [r] Remove option  [c] Continue: a

Enter new option name: Phone C
Identified options:
1. Phone A
2. Phone B
3. Phone C
[a] Add option  [r] Remove option  [c] Continue: c

Identified criteria:
1. battery_life (benefit)
2. price (cost)
[a] Add criterion  [r] Remove criterion  [c] Continue: c

Confirm criteria types:
1. battery_life → benefit
2. price → cost
Enter criterion number to toggle (or 'done'): done

Criterion: battery_life
Proposed order (worst → best):
1. poor
2. average
3. good
4. excellent
This order defines what is considered better for comparison.
Is this order correct for you? (y/n): y

Enter attributes for options (press Enter to skip):
Option: Phone A
Option: Phone B
Option: Phone C
battery_life: Best
price (USD): expensive

Rank criteria by importance (1 = highest priority):
battery_life: 1
price: 2

Criteria: {'battery_life': {'type': 'benefit', 'scale': ['poor', 'average', 'good', 'excellent'], 'unit': None, 'description': 'The quality of battery life in terms of duration and performance.'}, 'price': {'type': 'cost', 'scale': None, 'unit': 'USD', 'description': 'The cost of the phone.'}}

Mapped attributes: {'Phone A': {'battery_life': 2, 'price': None}, 'Phone B': {'battery_life': 4, 'price': None}, 'Phone C': {'battery_life': None, 'price': None}}

Ranked Results:
Phone B: 1.0
Phone A: 0.0
Phone C: 0.0
```

- Well mjor flaws, that is when i add a new option it should ask for attribute next and not at the end and when it asked for attribute and even when i inputted it the mapped attribute is still none for phone c
- My question is when a user adds a new option and adds a criteria for it, should t again go to the structure agent so it becomes more reliable?

- okk so no more sending it back to the ai, ive done all the changes now its time for the test phase again

```text
Describe your decision problem:
Type 'done' on a new line when finished.
> I want to buy a phone.
> Battery life matters more than price.
> Phone A is cheap but average battery.
> Phone B is expensive but excellent battery.
> done

Identified options:
1. Phone A
2. Phone B
[a] Add option  [r] Remove option  [c] Continue: a

Enter new option name: Xiaomi 15
Enter attributes for Xiaomi 15 (press Enter to skip):
battery_life: 1000mah
Invalid value. Allowed: poor, average, good, excellent
battery_life: average
price (USD): 750

Identified options:
1. Phone A
2. Phone B
3. Xiaomi 15
[a] Add option  [r] Remove option  [c] Continue: c

Identified criteria:
1. battery_life (benefit)
2. price (cost)
[a] Add criterion  [r] Remove criterion  [c] Continue: a

Enter criterion name: Weight
Is this a benefit or cost? (b = benefit, c = cost): c

Identified criteria:
1. battery_life (benefit)
2. price (cost)
3. weight (cost)
[a] Add criterion  [r] Remove criterion  [c] Continue: c

Confirm criteria types:
1. battery_life → benefit
2. price → cost
3. weight → cost
Enter criterion number to toggle (or 'done'): done

Criterion: battery_life
Proposed order (worst → best):
1. poor
2. average
3. good
4. excellent
This order defines what is considered better for comparison.
Is this order correct for you? (y/n): y

Enter attributes for options (press Enter to skip):
Option: Phone A
weight: 200 Grams
Option: Phone B
weight: 150 grams

Rank criteria by importance (1 = highest priority):
battery_life: 1
price: 2
weight: 3

Criteria: {'battery_life': {'type': 'benefit', 'scale': ['poor', 'average', 'good', 'excellent'], 'unit': None, 'description': 'The quality of battery life in terms of duration and performance.'}, 'price': {'type': 'cost', 'scale': None, 'unit': 'USD', 'description': 'The cost of the phone.'}, 'weight': {'type': 'cost', 'description': 'User-added criterion', 'scale': [], 'unit': None}}

Mapped attributes: {'Phone A': {'battery_life': 2, 'price': None, 'weight': None}, 'Phone B': {'battery_life': 4, 'price': None, 'weight': None}, 'Xiaomi 15': {'battery_life': 2, 'price': 750.0, 'weight': None}}

Ranked Results:
Phone B: 1.0
Xiaomi 15: 0.4
Phone A: 0.0
```

- Okk i typed in the weight of each phones why is it still None?
- weight (enter number only, unit: grams):
- This will take away the confusion, so lets implement it
- So if i remove the prompt_missing_attributes what will happen exactly?

```python
def confirm_options(options: dict, criteria: dict) -> dict:
    while True:
        print("\nIdentified options:")
        keys = list(options.keys())

        for i, opt in enumerate(keys, start=1):
            print(f"{i}. {opt}")

        choice = input("\n[a] Add option  [r] Remove option  [c] Continue: ").strip().lower()

        if choice == "c":
            break

        elif choice == "a":
            name = input("Enter new option name: ").strip()
            if not name:
                continue

            options[name] = {}
            print(f"\nEnter attributes for {name} (press Enter to skip):")

            for raw_c, meta in criteria.items():
                c = normalize_key(raw_c)
                scale = meta.get("scale")
                unit = meta.get("unit")

                if scale:
                    prompt = f"  {raw_c} (choose from: {', '.join(scale)}): "
                else:
                    unit_label = f", unit: {unit}" if unit else ""
                    prompt = f"  {raw_c} (enter number only{unit_label}): "

                while True:
                    val = input(prompt).strip()
                    if not val:
                        break

                    if scale:
                        norm_val = normalize_key(val)
                        scale_norm = [normalize_key(s) for s in scale]
                        if norm_val not in scale_norm:
                            print(f"  Invalid value. Allowed: {', '.join(scale)}")
                            continue
                        options[name][c] = val
                        break
                    else:
                        try:
                            options[name][c] = float(val)
                            break
                        except ValueError:
                            print("  Invalid value. Please enter a number only.")

        elif choice == "r":
            idx = input("Enter option number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(keys):
                    options.pop(keys[i])
    return options

def confirm_criteria(criteria: dict) -> dict:
    while True:
        print("\nIdentified criteria:")
        keys = list(criteria.keys())

        for i, k in enumerate(keys, start=1):
            ctype = criteria[k].get("type", "unknown")
            print(f"{i}. {k} ({ctype})")

        choice = input("\n[a] Add criterion  [r] Remove criterion  [c] Continue: ").strip().lower()

        if choice == "c":
            break

        elif choice == "a":
            name = input("Enter criterion name: ").strip()
            if not name:
                continue
            key = normalize_key(name)
            ctype = input("Is this a benefit or cost? (b = benefit, c = cost): ").strip().lower()
            unit = input("Enter unit (or press Enter if not applicable): ").strip()
            criteria[key] = {
                "type": "benefit" if ctype == "b" else "cost",
                "description": "User-added criterion",
                "scale": [],
                "unit": unit if unit else None
            }
        elif choice == "r":
            idx = input("Enter criterion number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(keys):
                    criteria.pop(keys[i])
    return criteria

def prompt_missing_attributes(options: dict, criteria: dict) -> dict:
    print("\nEnter attributes for options (press Enter to skip):")
    for option, attrs in options.items():
        print(f"\nOption: {option}")
        for raw_c, meta in criteria.items():
            c = normalize_key(raw_c)
            if c in attrs:
                continue
            unit = meta.get("unit")
            label = f"{raw_c} ({unit})" if unit else raw_c
            val = input(f"  {label}: ").strip()
            if val:
                try:
                    val = float(val)
                except ValueError:
                    pass
                attrs[c] = val
    return options
```

- This is how all 3 looks now , but in confirm_criteria its a warning saying that options[name][c] = float(val) "options" is not defined

```python
else:
    try:
        options[name][c] = float(val)
        break
    except ValueError:
        print("  Invalid value. Please enter a number only.")
```

- this should be where now?

```python 
def confirm_options(options: dict, criteria: dict) -> dict:
    while True:
        print("\nIdentified options:")
        keys = list(options.keys())

        for i, opt in enumerate(keys, start=1):
            print(f"{i}. {opt}")

        choice = input("\n[a] Add option  [r] Remove option  [c] Continue: ").strip().lower()

        if choice == "c":
            break

        elif choice == "a":
            name = input("Enter new option name: ").strip()
            if not name:
                continue

            options[name] = {}
            print(f"\nEnter attributes for {name} (press Enter to skip):")

            for raw_c, meta in criteria.items():
                c = normalize_key(raw_c)
                scale = meta.get("scale")
                unit = meta.get("unit")

                if scale:
                    prompt = f"  {raw_c} (choose from: {', '.join(scale)}): "
                else:
                    unit_label = f", unit: {unit}" if unit else ""
                    prompt = f"  {raw_c} (enter number only{unit_label}): "

                while True:
                    val = input(prompt).strip()
                    if not val:
                        break

                    if scale:
                        norm_val = normalize_key(val)
                        scale_norm = [normalize_key(s) for s in scale]
                        if norm_val not in scale_norm:
                            print(f"  Invalid value. Allowed: {', '.join(scale)}")
                            continue
                        options[name][c] = val
                        break
                    else:
                        try:
                            options[name][c] = float(val)
                            break
                        except ValueError:
                            print("  Invalid value. Please enter a number only.")

        elif choice == "r":
            idx = input("Enter option number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(keys):
                    options.pop(keys[i])
    return options
```

- What about now?
- Earlier i could atleast add the attributes foe the options and now the whole weight Criteria is GONE , like its not even in the MAPPED ATTRIBUTES

```python
def confirm_criteria(criteria: dict) -> dict:
    while True:
        print("\nIdentified criteria:")
        keys = list(criteria.keys())

        for i, k in enumerate(keys, start=1):
            ctype = criteria[k].get("type", "unknown")
            print(f"{i}. {k} ({ctype})")

        choice = input("\n[a] Add criterion  [r] Remove criterion  [c] Continue: ").strip().lower()

        if choice == "c":
            break

        elif choice == "a":
            name = input("Enter criterion name: ").strip()
            if not name:
                continue
            key = normalize_key(name)
            ctype = input("Is this a benefit or cost? (b = benefit, c = cost): ").strip().lower()
            unit = input("Enter unit (or press Enter if not applicable): ").strip()
            criteria[key] = {
                "type": "benefit" if ctype == "b" else "cost",
                "description": "User-added criterion",
                "scale": [],
                "unit": unit if unit else None
            }
        elif choice == "r":
            idx = input("Enter criterion number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(keys):
                    criteria.pop(keys[i])
    return criteria
```

- just modify it, my head is spinning atp
- Invalid value. Please enter a number only (e.g., 200). Invalid value. Please enter a number only (e.g., 200).
- I cant get my head around why this was printed twice
- Well there's one more thing well after when the structure agent maps the benefit and the cost, it asks the user to pick the number to invert it right? it looks confusing at first or its just typing done to get out of it.. which is kinda.. meh.. i mean its okay.. but the problem is once user types 1 or 2 to swap the benefit / cost there's isnt another print statement , so no visualisation if that has inverted or not

- Dude i can feel that this is like near completion and i'm hoping that the explanation_agent doesn't have much hassle
- I dont have a structure_decision like as such.. I can share the structre_agent.py. I'm using the OPEN AI API. I can add the "Strongly recommended hardening (next step)" im using gpt 4o mini rn. I mean as long as im only using text prompts right? so I have like 10$ remaining in the budget and i havent like used 10 cents ig.

```python
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment")
client = OpenAI(api_key=API_KEY)

STRUCTURE_SYSTEM_PROMPT = """
You are an assistive decision-structuring agent.
Your role is to HELP the user structure a decision problem.
You DO NOT make decisions.
You must PRODUCE A DRAFT STRUCTURE that the USER will review and confirm.
Your responsibilities are to SUGGEST:
The decision goal
A list of options
A list of evaluation criteria

For EACH criterion you MUST:
Classify it as either:
• "benefit" (higher values are better), or
• "cost" (lower values are better)

If the criterion is QUALITATIVE:
• You MUST provide an explicit ordinal scale
• The scale MUST be ordered from lowest → highest
• Example: ["cheap", "affordable", "expensive"]

If the criterion is NUMERIC:
• You MUST specify a unit (e.g. "USD", "grams", "hours")
• You MUST NOT provide a scale
Extract raw numeric values when the user provides numbers
Use descriptive terms ONLY if numeric values are not available
Use "unknown" when information is missing

IMPORTANT:
All cost/benefit classifications are PROVISIONAL
The user will confirm or edit them
Prefer being explicit over being brief

You MUST NOT:
Assign weights
Score options
Rank options
Convert descriptors into numbers
Recommend any option

Output ONLY valid JSON matching the schema.
Do not include explanations outside the JSON.
"""

STRUCTURE_SCHEMA_DESCRIPTION = """
Return JSON in the following format:
{
"decision_goal": string,
"criteria": {
"<criterion_name>": {
  "type": "benefit | cost",
  "scale": [string],
  "unit": string | null,
  "description": string
}
},
"options": {
"<option_name>": {
  "<criterion_name>": number | string | "unknown"
}
},
"assumptions": [string],
"unknowns": [string]
}
"""

def structure_decision(user_input: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": STRUCTURE_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"User decision description:\n\"\"\"{user_input}\"\"\"\n{STRUCTURE_SCHEMA_DESCRIPTION}"
            }
        ],
    )
    content = response.choices[0].message.content.strip()
    try:
        structured_data = json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError("Structure Agent returned invalid JSON") from e
    return structured_data
```

```text
I want to buy a phone.
Battery life matters more than price.
Phone A is cheap but average battery.
Phone B costs 40,000 INR and good battery
Xiaomi 15 costs 70,000 rupees has excellent battery life
Iphone 15 costs 80,000 rupees has an decent battery

Im just gonna type exactly like this
```

- nah nah We are doing extreme testing. Suppose i want to travel from Pathanamthitta to Munnar on a bike.Suppose there are 4 routes, just search the web for that pls. for this ik how the condition of all . Assign the route 2 and 4, has less pot holes . Route 1 have the best scenic roads. Route 3 is the longest, but is longest and also have excellent scenes.Distance is my least priority. Scenary and roads are my top priority.. so... like structure an input like that so that i can test EVERYTHING, also dont name routes like 1,2,3,4 make some names.
- nah we're gonna stress test it, but this time we're gonna add in numbers as well into the mix, also what all be should be added into the mix so it proves to be a stress tester?

```text 
resolve_scale_mismatch()  this is absolutely necessary and i like the
The value "mostly_good" is not in the scale.
Choose how to resolve this:
[a] Add to scale
[m] Map to existing value
[i] Ignore this value
[e] Edit entire scale
```

- while adding it should add it to the scale and move the rest of the values downward or to the right if in like the list

```python
def confirm_ordinal_scales(criteria, options):
    for raw_key, meta in criteria.items():
        key = normalize_key(raw_key)
        scale = meta.get("scale")
        if not scale:
            continue

        print("\nCriterion:", raw_key)
        print("Proposed order (worst → best):")
        for i, v in enumerate(scale, start=1):
            print(f"{i}. {v}")

        print("\nThis order defines what is considered better for comparison.")
        choice = input("Is this order correct for you? (y/n): ").strip().lower()

        if choice != "y":
            new_scale = input("Enter corrected scale (comma-separated, lowest → highest): ").strip()
            if new_scale:
                meta["scale"] = [s.strip() for s in new_scale.split(",")]

        detected = set()
        for opt_vals in options.values():
            val = opt_vals.get(key)
            if isinstance(val, str):
                detected.add(normalize_key(val))

        scale_norm = [normalize_key(s) for s in meta["scale"]]
        missing = detected - set(scale_norm)

        if missing:
            print(f'\nDetected values for "{raw_key}": {", ".join(detected)}')
            print(f"Your scale does not include: {', '.join(missing)}")
            proceed = input("Proceed anyway? (y/n): ").strip().lower()
            if proceed != "y":
                return confirm_ordinal_scales(criteria, options)
    return criteria
```

- Update this as ive alread modified the input_helpers.py with resolve_scale_mismatch
- in the new confirm_ordinal_scales there's no normalized={}
- or the normalized_key = meta so it isnt needed right?
- give me a comit msg for today im soo sleepy that my brain cant come up with anything anymore

```text
(.venv) PS G:\Decision-Lens\src> python main.py
Describe your decision problem:
Type 'done' on a new line when finished.
> I want to choose a weekend bike ride.
> I care most about scenic beauty and road condition.
> Distance and travel time are less important.
> Here are my options:
> Mountain Loop:
> Around 160 km.
> Extremely scenic with mountain views.
> Roads are mostly good but narrow.
> Takes about 6 hours.
> Coastal Ride:
> About 120 km.
> Decent scenery along the coast.
> Smooth roads but crowded.
> Travel time is unpredictable.
> Forest Shortcut:
> Roughly 90 km.
> Very scenic but has bad potholes.
> Fastest route.
> Highway Sprint:
> Around 80 km.
> Not scenic.
> Excellent road condition.
> Takes about 2 hours.
> done

Identified options:
1. Mountain Loop
2. Coastal Ride
3. Forest Shortcut
4. Highway Sprint

[a] Add option  [r] Remove option  [c] Continue: a
Enter new option name: Gap Road
Enter attributes for Gap Road (press Enter to skip):
scenic_beauty (choose from: not scenic, decent scenery, very scenic, extremely scenic): not scenic
road_condition (choose from: bad potholes, narrow but mostly good, smooth, excellent): excellent
distance (enter number only, unit: km): 160kms
Invalid value. Please enter a number only.
distance (enter number only, unit: km): 160
travel_time (enter number only, unit: hours): 1.25

Identified options:
1. Mountain Loop
2. Coastal Ride
3. Forest Shortcut
4. Highway Sprint
5. Gap Road
[a] Add option  [r] Remove option  [c] Continue: c

Identified criteria:
1. scenic_beauty (benefit)
2. road_condition (benefit)
3. distance (cost)
4. travel_time (cost)
[a] Add criterion  [r] Remove criterion  [c] Continue: c

Confirm criteria types:
1. scenic_beauty → benefit
2. road_condition → benefit
3. distance → cost
4. travel_time → cost
Type numbers to toggle, 'done' when satisfied.
Enter criterion number to toggle (or 'done'): done

Criterion: scenic_beauty
Proposed order (worst → best):
1. not scenic
2. decent scenery
3. very scenic
4. extremely scenic
This order defines what is considered better for comparison.
Is this order correct for you? (y/n): n
Enter corrected scale (comma-separated, lowest → highest): meh, okay, good,excellent,pristine

The value "very_scenic" is not in the scale.
Choose how to resolve this:
[a] Add to scale
[m] Map to existing value
[i] Ignore this value
[e] Edit entire scale
Choice: i

The value "decent_scenery" is not in the scale.
Choose how to resolve this:
[a] Add to scale
[m] Map to existing value
[i] Ignore this value
[e] Edit entire scale
Choice: i

The value "not_scenic" is not in the scale.
Choose how to resolve this:
[a] Add to scale
[m] Map to existing value
[i] Ignore this value
[e] Edit entire scale
Choice: i

The value "extremely_scenic" is not in the scale.
Choose how to resolve this:
[a] Add to scale
[m] Map to existing value
[i] Ignore this value
[e] Edit entire scale
Choice: i

Criterion: road_condition
Proposed order (worst → best):
1. bad potholes
2. narrow but mostly good
3. smooth
4. excellent
This order defines what is considered better for comparison.
Is this order correct for you? (y/n): y

Rank criteria by importance (1 = highest priority):
scenic_beauty: 1
road_condition: 2
distance: 3
travel_time: 4

Criteria: {'scenic_beauty': {'type': 'benefit', 'scale': ['meh', 'okay', 'good', 'excellent', 'pristine'], 'unit': None, 'description': 'The level of scenic beauty along the bike ride', 'ignored_values': {'very_scenic', 'decent_scenery', 'not_scenic', 'extremely_scenic'}}, 'road_condition': {'type': 'benefit', 'scale': ['bad potholes', 'narrow but mostly good', 'smooth', 'excellent'], 'unit': None, 'description': 'The condition of the roads along the bike ride'}, 'distance': {'type': 'cost', 'unit': 'km', 'description': 'The total distance of the bike ride'}, 'travel_time': {'type': 'cost', 'unit': 'hours', 'description': 'The estimated time to complete the bike ride'}}

Mapped attributes: {'Mountain Loop': {'scenic_beauty': None, 'road_condition': 2, 'distance': 160, 'travel_time': 6}, 'Coastal Ride': {'scenic_beauty': None, 'road_condition': 3, 'distance': 120, 'travel_time': None}, 'Forest Shortcut': {'scenic_beauty': None, 'road_condition': 1, 'distance': 90, 'travel_time': None}, 'Highway Sprint': {'scenic_beauty': None, 'road_condition': 4, 'distance': 80, 'travel_time': 2}, 'Gap Road': {'scenic_beauty': None, 'road_condition': 4, 'distance': 160.0, 'travel_time': 1.25}}

Ranked Results:
Highway Sprint: 0.974
Gap Road: 0.667
Coastal Ride: 0.6
Forest Shortcut: 0.35
Mountain Loop: 0.167
```

```python 
from utils.normalization import normalize_key

def normalize_text(value: str) -> str:
    return value.strip().lower()

def map_attributes(structured_data: dict) -> dict:
    criteria = structured_data.get("criteria", {})
    options = structured_data.get("options", {})
    normalized_criteria = {normalize_key(k): v for k, v in criteria.items()}
    mapped = {}

    for option, attrs in options.items():
        mapped[option] = {}
        for raw_criterion, raw_value in attrs.items():
            c_key = normalize_key(raw_criterion)
            if raw_value == "unknown":
                mapped[option][c_key] = None
                continue
            meta = normalized_criteria.get(c_key)
            if not meta:
                mapped[option][c_key] = None
                continue
            if isinstance(raw_value, (int, float)):
                mapped[option][c_key] = raw_value
                continue
            scale = meta.get("scale")
            if not scale:
                mapped[option][c_key] = None
                continue
            scale_norm = [normalize_key(s) for s in scale]
            value_norm = normalize_key(str(raw_value))
            if value_norm not in scale_norm:
                mapped[option][c_key] = None
                continue
            mapped[option][c_key] = scale_norm.index(value_norm) + 1
    return mapped
```

- we'll do fix 1 of adding a warning and also fix 2 of offer "map all" where if the user selects m Auto map similar values then it will suggest and will show the suggested mapping page and can prompt if they accept it or not, so in the end user is fully under control and nothing breaks
- well, this is a good point to anothr support. when the rankings are listed. The program ends. But for a user, his decison can be changed after he saw the rankings, so we are not allowing him to change the options and criteria. the program just stops. what if he have to modify it again?

```python
def main():
    # 1. Multiline human input
    user_input = get_multiline_input("Describe your decision problem:")

    # 2. AI-assisted structuring (DRAFT)
    structured = structure_decision(user_input)
    criteria = structured.get("criteria", {})
    options = structured.get("options", {})

    if not criteria or not options:
        print("Could not extract sufficient decision structure.")
        return

    # 3. User confirms / edits OPTIONS
    options = confirm_options(options,criteria)

    # 4. User confirms / edits CRITERIA
    criteria = confirm_criteria(criteria, options)

    # 5. User confirms cost vs benefit
    criteria = confirm_criteria_types(criteria)

    # 6. User confirms ordinal scales
    criteria = confirm_ordinal_scales(criteria, options)

    # Warn if criteria have no data across all options
    for c in criteria:
        if all(options.get(opt, {}).get(c) in (None, "unknown") for opt in options):
            print(f"\nWarning: Some criteria have no data for any option. Results may be inconclusive.")
            break

    # 8. User ranks criteria (importance)
    criterion_names = list(criteria.keys())
    weights = get_weights_from_ranking(criterion_names)

    # 9. Prepare criteria types for engine
    criteria_types = {c: meta["type"] for c, meta in criteria.items()}

    # 10. Attribute mapping (descriptors → numbers)
    mapped_attributes = map_attributes({"criteria": criteria, "options": options})

    # 12. Output results
    while True:
        results = compute_weighted_scores(
            options=list(mapped_attributes.keys()),
            criteria=criterion_names,
            weights=weights,
            values=mapped_attributes,
            criteria_types=criteria_types
        )

        print("\nRanked Results:")
        for option, score in results.items():
            print(f"{option}: {score}")

        choice = post_result_menu()

        if choice == "0":
            print("\nDecision finalized. Exiting.")
            break
        elif choice == "1":
            weights = get_weights_from_ranking(criterion_names)
        elif choice == "2":
            options = prompt_missing_attributes(options, criteria)
            mapped_attributes = map_attributes({"criteria": criteria, "options": options})
        elif choice == "3":
            options = confirm_options(options, criteria)
            mapped_attributes = map_attributes({"criteria": criteria, "options": options})
        elif choice == "4":
            criteria = confirm_criteria(criteria)
```


        criteria = confirm_criteria_types(criteria)

        criteria = confirm_ordinal_scales(criteria, options)



        criterion_names = list(criteria.keys())

        criteria_types = {c: meta["type"] for c, meta in criteria.items()}



        mapped_attributes = map_attributes({

            "criteria": criteria,

            "options": options

        })



    elif choice == "5":

        continue



    else:

        print("Invalid choice.")

if name == "main":

try:

    main()

except KeyboardInterrupt:

    print("\nOperation cancelled by user.")
```
- why am i getting a prompt_missing_attributes?

```text
well there's one more debugging hell.. when i change the
⚠ Warning: Ignoring this value will remove usable data for some options under "road_condition". Proceed anyway? (y/n): y The value "smooth" is not in the scale. Choose how to resolve this: [a] Add to scale [m] Map to existing value [i] Ignore this value [e] Edit entire scale Choice: a Current scale (lowest → highest): 1. crap 2. pocket road Insert 'smooth' at position (1–3): 3 The value "excellent" is not in the scale. Choose how to resolve this: [a] Add to scale [m] Map to existing value [i] Ignore this value [e] Edit entire scale Choice: a Current scale (lowest → highest): 1. crap 2. pocket road 3. smooth Insert 'excellent' at position (1–4): 4 The value "bad_potholes" is not in the scale. Choose how to resolve this: [a] Add to scale [m] Map to existing value [i] Ignore this value [e] Edit entire scale Choice: m Map to: 1. crap 2. pocket road 3. smooth 4. excellent Choose number: 1
```

- well there's one more debugging hell.. when i change the
- After changing the last criteria in roads it doesn't show thr changes it just goes to the next option so the changes cant be visualised

```python
def resolve_scale_mismatch(
    criterion_name: str,
    scale: list[str],
    unknown_values: set[str]
) -> tuple[list[str], dict[str, str], set[str]]:
    """
    Returns:
    - updated_scale
    - alias_map (e.g. {"mostly_good": "okay"})
    - ignored_values
    """

    alias_map = {}
    ignored = set()

    # Helper: suggest mappings by relative position / similarity
    def suggest_mappings(values, scale):
        suggestions = {}
        for v in values:
            # very simple heuristic: map by keywords
            v_norm = v.replace("_", " ")
            if "extreme" in v_norm or "excellent" in v_norm:
                suggestions[v] = scale[-1]
            elif "very" in v_norm or "good" in v_norm:
                suggestions[v] = scale[-2] if len(scale) >= 2 else scale[-1]
            elif "decent" in v_norm or "okay" in v_norm:
                suggestions[v] = scale[len(scale)//2]
            elif "not" in v_norm or "poor" in v_norm:
                suggestions[v] = scale[0]
        return suggestions

    for val in unknown_values:
        print(f'\nThe value "{val}" is not in the scale.')

        while True:
            choice = input(
                "\nChoose how to resolve this:\n"
                "[a] Add to scale\n"
                "[m] Map to existing value\n"
                "[i] Ignore this value\n"
                "[e] Edit entire scale\n"
                "Choice: "
            ).strip().lower()

            # ---------------- ADD TO SCALE ----------------
            if choice == "a":
                print("\nCurrent scale (lowest → highest):")
                for i, s in enumerate(scale, start=1):
                    print(f"{i}. {s}")

                pos = input(
                    f"Insert '{val}' at position (1–{len(scale)+1}): "
                ).strip()

                if pos.isdigit():
                    idx = int(pos) - 1
                    if 0 <= idx <= len(scale):
                        scale.insert(idx, val)
                        break

            # ---------------- MAP TO EXISTING ----------------
            elif choice == "m":
                print("\nMap to:")
                for i, s in enumerate(scale, start=1):
                    print(f"{i}. {s}")

                sel = input("Choose number: ").strip()
                if sel.isdigit():
                    idx = int(sel) - 1
                    if 0 <= idx < len(scale):
                        alias_map[val] = scale[idx]
                        break

            # ---------------- IGNORE (FIX 1) ----------------
            elif choice == "i":
                # Warn if this is destructive
                remaining = unknown_values - ignored - {val}
                if not remaining:
                    print(
                        f"\n⚠ WARNING:\n"
                        f"Ignoring this value will leave NO usable data for "
                        f'"{criterion_name}".\n'
                        "This criterion may be ignored entirely in scoring."
                    )
                else:
                    print(
                        f"\n⚠ Warning: Ignoring this value will remove "
                        f"usable data for some options under "
                        f'"{criterion_name}".'
                    )

                confirm = input("Proceed anyway? (y/n): ").strip().lower()
                if confirm == "y":
                    ignored.add(val)
                    break
                else:
                    continue

            # ---------------- EDIT ENTIRE SCALE (FIX 2) ----------------
            elif choice == "e":
                new_scale = input(
                    "Enter new scale (comma-separated, lowest → highest): "
                ).strip()

                if not new_scale:
                    continue

                scale[:] = [s.strip() for s in new_scale.split(",")]

                print(
                    f"\nYou replaced the scale for '{criterion_name}'.\n"
                    "Detected existing values:"
                )
                for v in unknown_values:
                    print(f"- {v}")

                followup = input(
                    "\nHow would you like to handle existing values?\n"
                    "[a] Map each value manually\n"
                    "[m] Auto-map similar values (review before applying)\n"
                    "[i] Ignore all existing values\n"
                    "Choice: "
                ).strip().lower()

                # Auto-map similar
                if followup == "m":
                    suggestions = suggest_mappings(unknown_values, scale)
                    print("\nSuggested mappings:")
                    for k, v in suggestions.items():
                        print(f"{k} → {v}")

                    if input("Apply these mappings? (y/n): ").strip().lower() == "y":
                        alias_map.update(suggestions)
                    break

                # Manual mapping
                elif followup == "a":
                    for v in unknown_values:
                        print(f"\nMap '{v}' to:")
                        for i, s in enumerate(scale, start=1):
                            print(f"{i}. {s}")
                        sel = input("Choose number (or Enter to skip): ").strip()
                        if sel.isdigit():
                            idx = int(sel) - 1
                            if 0 <= idx < len(scale):
                                alias_map[v] = scale[idx]
                    break

                # Ignore all (with warning)
                elif followup == "i":
                    print(
                        f"\n⚠ WARNING:\n"
                        f"Ignoring all values will leave NO usable data for "
                        f'"{criterion_name}".'
                    )
                    if input("Proceed anyway? (y/n): ").strip().lower() == "y":
                        ignored.update(unknown_values)
                    break



return scale, alias_map, ignored
```

- So , inn here fix the flow as well as call it after every succesful action as well..
- Ive already defined the print_scale funcition in input_helpers
- okk so how do i do the Optional enhancement 
```python
for c in normalized_criteria:
mapped[option].setdefault(c, None)
```
- I mean if its not necessary, then..
- there is one thing the debubg print statemts only work in the first  run and after run if i change the options , it wont work
- there is one thing the debubg print statemts in main.py only work in the first  run and after run if i change the options , it wont work so that i cant see the mapped attributes and everthing for debugging
- We'll go with fix 2, 
- okk so now i want you to give me a specific domain example for example i am in a restaurat and i want to eat a dish . give 4 specific dish names let there be numeric values as well as ordinal values. for price sy one as 1,200 rupees other as 500 RS . Also include calories and protein. My aim is to eat an afoordable protein rich food which is tasty as well
- <pasted the debug op> I mean i cant change the ranking, like if i prioritize one over the other after seeing the results i cant change the ranking now
- plus on the previous run the wording was affordability and it was quite confusing. maybe its a structure agent problem

```text
STRUCTURE_SYSTEM_PROMPT = """

You are an assistive decision-structuring agent.

Your role is to HELP the user structure a decision problem.

You DO NOT make decisions.

You must PRODUCE A DRAFT STRUCTURE that the USER will review and confirm.

Your responsibilities are to SUGGEST:

The decision goal

A list of options

A list of evaluation criteria


For EACH criterion you MUST:

Classify it as either:

• "benefit" (higher values are better), or

• "cost" (lower values are better)

If the criterion is QUALITATIVE:

• You MUST provide an explicit ordinal scale

• The scale MUST be ordered from lowest → highest

• Example: ["cheap", "affordable", "expensive"]

If the criterion is NUMERIC:

• You MUST specify a unit (e.g. "USD", "grams", "hours")

• You MUST NOT provide a scale

Extract raw numeric values when the user provides numbers

Use descriptive terms ONLY if numeric values are not available

Use "unknown" when information is missing


IMPORTANT NAMING RULE:

Criterion names must refer to the RAW MEASURABLE ATTRIBUTE

Do NOT use derived or interpretive names such as:

"affordability", "value", "quality", "overall goodness"

Use concrete attributes instead:

"price", "cost", "calories", "protein", "time", "distance"

The interpretation (e.g., affordability) will be handled later via cost/benefit and weighting


IMPORTANT:

All cost/benefit classifications are PROVISIONAL

The user will confirm or edit them

Prefer being explicit over being brief


You MUST NOT:

Assign weights

Score options

Rank options

Convert descriptors into numbers

Recommend any option


Output ONLY valid JSON matching the schema.

Do not include explanations outside the JSON.

"""
```
- Ig this is okay?
- okk give me another stress testing prompt so that i can test every single thing thorughly
- well one thing i noticed is that while ranking, like there was no reprentation of the criterias , without seeing all the criterias, user cant effectively provide a ranking. Also, I ranked driving feel and price with the same number.. uh.. should that be the case?

- Show a criteria summary before ranking
Enforce unique ranks (no ties)

- If no numeric values are provided for a measurable attribute, prefer a qualitative ordinal scale.
I had added this rule to the prompt and yet
<pasted the debug>

```text
File "G:\Decision-Lens\src\main.py", line 175, in <module>

main()

~~~~^^

File "G:\Decision-Lens\src\main.py", line 79, in main

criteria = confirm_ordinal_scales(criteria, options)

File "G:\Decision-Lens\src\utils\input_helpers.py", line 149, in confirm_ordinal_scales

for raw_key, meta in criteria.items():

                     ^^^^^^^^^^^^^^

AttributeError: 'NoneType' object has no attribute 'items'

(.venv) PS G:\Decision-Lens\src>
```

- ig we'll integrate because i think if this is not done, it might mess up the logics and the flow
``` text
if no scale AND no numeric data:

ask user to define a scale  
 or he can skip it

confirm scale (existing or newly created)

detect mismatches

resolve mismatches
```
- there should be choices, some are lazy and they just want something

```text
Add three choices at scale-missing moments
✔ Default suggestion = Define scale
✔ Provide Auto-generate for lazy users
✔ Make Ignore explicit, never silent
```
- Yess this is right and the auto generated scale can be editable later as well
Give me that

- --pasted the code-- this is the current confirm_ordinal_scales so i dont want you to mess up what is working right now only add new features
also each comment should be untouched and if adding new blocks it should be commented as well
- let me test it
- --pasted debug--
- I think everything is working as expected and the system has matured
- okk give me a commit msg for today for all the problems identified fixes and in the next commit we're gonna implement the explanation agent
- We're in the final stages..  Explanation Agent is the easy part
- Ig well go with the AI assisted Explanation Agent? that would be the logical choice right?

```text
Design the exact Explanation Agent prompt

Implement the deterministic explanation payload builder what exactly is this deterministic explanation payload builder?

Well, i need it such a way that, at the end it produces an explanation and suppose when the user edits the option or criteria and when the engine provides a ranking it should produce an output then as well.. Bascially it should explain along with the changing rankings
```

```python
from agents.structure_agent import structure_decision

from core.attribute_mapper import map_attributes

from core.decision_engine import compute_weighted_scores

from utils.input_helpers import (

get_weights_from_ranking,

confirm_criteria_types,

confirm_ordinal_scales,

get_multiline_input,

confirm_options,

confirm_criteria,

post_result_menu,

)

🔧 Debug flag - IF SET TO True-> it would be seen in terminal , IF SET TO False -> Hidden

DEBUG = True

def debug_state(criteria, weights, mapped_attributes):

print("\n--- DEBUG STATE ---")

print("Criteria:")

for c, meta in criteria.items():

    print(f"  {c}: {meta}")



print("\nWeights:")

for c, w in weights.items():

    print(f"  {c}: {round(w, 3)}")



print("\nMapped attributes:")

for opt, vals in mapped_attributes.items():

    print(f"  {opt}: {vals}")



print("-------------------\n")

def show_criteria_summary(criteria):  #To see criteria summary before ranking

print("\nCriteria summary (for ranking):")

for i, (c, meta) in enumerate(criteria.items(), start=1):

    ctype = meta["type"]

    unit = meta.get("unit")

    scale = meta.get("scale")



    if scale:

        print(

            f"{i}. {c} ({ctype}) → scale: "

            f"{' < '.join(scale)}"

        )

    else:

        unit_label = f", unit: {unit}" if unit else ""

        print(f"{i}. {c} ({ctype}{unit_label})")

def main():

# 1. Multiline human input

user_input = get_multiline_input(

    "Describe your decision problem:"

)



# 2. AI-assisted structuring (DRAFT)

structured = structure_decision(user_input)



criteria = structured.get("criteria", {})

options = structured.get("options", {})



if not criteria or not options:

    print("Could not extract sufficient decision structure.")

    return



# 3. User confirms / edits OPTIONS

options = confirm_options(options, criteria)



# 4. User confirms / edits CRITERIA

criteria = confirm_criteria(criteria, options)



# 5. User confirms cost vs benefit

criteria = confirm_criteria_types(criteria)



# 6. User confirms ordinal scales

criteria = confirm_ordinal_scales(criteria, options)



# Warn if criteria have no data across all options

for c in criteria:

    if all(

        options.get(opt, {}).get(c) in (None, "unknown")

        for opt in options

    ):

        print(

            f"\nWarning: Some criteria have no data for any option. "

            "Results may be inconclusive."

        )

        break



# 7. User ranks criteria (importance)

criterion_names = list(criteria.keys())

show_criteria_summary(criteria)

weights = get_weights_from_ranking(criterion_names)



# 8. Prepare criteria types for engine

criteria_types = {

    c: meta["type"] for c, meta in criteria.items()

}



# 9. Attribute mapping (descriptors → numbers)

mapped_attributes = map_attributes({

    "criteria": criteria,

    "options": options

})



# 10. Main evaluation loop
while True:
    # Recompute results
    results = compute_weighted_scores(
        options=list(mapped_attributes.keys()),
        criteria=criterion_names,
        weights=weights,
        values=mapped_attributes,
        criteria_types=criteria_types
    )

    def build_explanation_payload(

        results: dict,

        normalized_values: dict,

        raw_values: dict,

        criteria: dict,

        weights: dict

    ) -> dict:

        """

        Builds a deterministic explanation payload from engine outputs.



        This payload contains ONLY factual, auditable data.

        It is safe to pass directly to an AI explanation renderer.

        """



        ranked_options = list(results.keys())



        # User priorities = highest-weighted criteria

        user_priorities = sorted(

            weights.keys(),

            key=lambda c: weights[c],

            reverse=True

        )[:3]



        payload = {

            "summary": {},

            "options": {},

            "user_priorities": user_priorities

        }



        # Score gap between top two (if available)

        if len(ranked_options) > 1:

            top = ranked_options[0]

            second = ranked_options[1]

            payload["summary"]["top_option"] = top

            payload["summary"]["score_gap_to_next"] = round(

                results[top] - results[second], 3

            )

        else:

            payload["summary"]["top_option"] = ranked_options[0]

            payload["summary"]["score_gap_to_next"] = None



        # Build per-option explanation facts

        for rank, option in enumerate(ranked_options, start=1):

            contributions = {}

            missing_criteria = []



            for criterion in criteria:

                norm_val = normalized_values.get(option, {}).get(criterion)



                if norm_val is None:

                    missing_criteria.append(criterion)

                    continue



                contributions[criterion] = norm_val * weights.get(criterion, 0)



            # Sort contributions

            positive_factors = sorted(

                contributions,

                key=contributions.get,

                reverse=True

            )



            negative_factors = sorted(

                contributions,

                key=contributions.get

            )



            payload["options"][option] = {

                "rank": rank,

                "score": results[option],

                "top_positive_factors": positive_factors[:3],

                "top_negative_factors": negative_factors[:3],

                "missing_criteria": missing_criteria,

                "applied_weights": {

                    c: weights[c]

                    for c in positive_factors[:3]

                }

            }



        return payload





    # 🔍 Debug output (always current)

    if DEBUG:

        debug_state(criteria, weights, mapped_attributes)



    # Show results

    print("\nRanked Results:")

    for option, score in results.items():

        print(f"{option}: {score}")



    # Post-result menu

    choice = post_result_menu()



    if choice == "0":

        print("\nDecision finalized. Exiting.")

        break



    elif choice == "1":

        weights = get_weights_from_ranking(criterion_names)



    elif choice == "2":

        options = confirm_options(options, criteria)

        mapped_attributes = map_attributes({

            "criteria": criteria,

            "options": options

        })



    elif choice == "3":

        criteria = confirm_criteria(criteria, options)

        criteria = confirm_criteria_types(criteria)

        criteria = confirm_ordinal_scales(criteria, options)



        criterion_names = list(criteria.keys())

        criteria_types = {

            c: meta["type"] for c, meta in criteria.items()

        }



        mapped_attributes = map_attributes({

            "criteria": criteria,

            "options": options

        })



        # 🔁 Ask if user wants to re-rank after changing criteria
        re_rank = input(
            "\nCriteria were modified. Do you want to re-rank their importance? (y/n): "
        ).strip().lower()

        if re_rank == "y":
            weights = get_weights_from_ranking(criterion_names)

    else:
        print("Invalid choice. Please try again.")

if name == "main":
try:
    main()
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
```

- okk i just moved
```python
def build_explanation_payload(
    results: dict,
    normalized_values: dict,
    raw_values: dict,
    criteria: dict,
    weights: dict
) -> dict:
```
- into core/explanation_builder.py

```text
xpose normalized values from the engine (this is non-negotiable)
Right now, your Explanation Builder expects:
normalized_values
I already have a normalization.py in utils and its
def normalize_key(key: str) -> str:
    return key.strip().lower().replace(" ", "_")
```

```python
explanation_payload = build_explanation_payload(
    results=results,
    normalized_values=normalized,
    raw_values=mapped_attributes,
    criteria=criteria,
    weights=weights
)
```
- this should be right after results,normalized=compute_weighted_scores() right? in the while True main evaluation loop?

- --pasted debug--

```python
from utils.normalization import normalize_key

def build_explanation_payload(
    results: dict,
    normalized_values: dict,
    raw_values: dict,
    criteria: dict,
    weights: dict
) -> dict:
    """
    Builds a deterministic explanation payload from engine outputs.

    This payload contains ONLY factual, auditable data.
    It is safe to pass directly to an AI explanation renderer.
    """

    ranked_options = list(results.keys())

    # User priorities = highest-weighted criteria
    user_priorities = sorted(
        weights.keys(),
        key=lambda c: weights[c],
        reverse=True
    )[:3]

    payload = {
        "summary": {},
        "options": {},
        "user_priorities": user_priorities
    }

    # Score gap between top two (if available)
    if len(ranked_options) > 1:
        top = ranked_options[0]
        second = ranked_options[1]
        payload["summary"]["top_option"] = top
        payload["summary"]["score_gap_to_next"] = round(
            results[top] - results[second], 3
        )
    else:
        payload["summary"]["top_option"] = ranked_options[0]
        payload["summary"]["score_gap_to_next"] = None

    # Build per-option explanation facts
    for rank, option in enumerate(ranked_options, start=1):
        contributions = {}
        missing_criteria = []

        for raw_criterion in criteria:
            c = normalize_key(raw_criterion)
            norm_val = normalized_values.get(option, {}).get(c)
            if norm_val is None:
                missing_criteria.append(criterion)
                continue

            contributions[criterion] = norm_val * weights.get(criterion, 0)

        # Sort contributions
        positive_factors = sorted(
            contributions,
            key=contributions.get,
            reverse=True
        )

        negative_factors = sorted(
            contributions,
            key=contributions.get
        )

        payload["options"][option] = {
            "rank": rank,
            "score": results[option],
            "top_positive_factors": positive_factors[:3],
            "top_negative_factors": negative_factors[:3],
            "missing_criteria": missing_criteria,
            "applied_weights": {
                c: weights[c]
                for c in positive_factors[:3]
            }
        }

    return payload
```
- Just modify it will ya, because the criterion is not defined
- --pasted debug again--
```python 
Contribution comes from normalized values
norm_val = normalized_values.get(option, {}).get(c)
if norm_val is None:
    continue

contributions[raw_criterion] = (
    norm_val * weights.get(raw_criterion, 0)
)
``` 
- So this in explanation builder should be changed right?
- --pasted debug again--
- can i ask something?when i typed in to manually set the scale it only asked me to map the fun part? was all the other scales automatically matched?

- okk theres one another ux thingy if i type in 1 to change the criteria importance at last it prompts to rank but here it doesnt show me what all to rank like im completely blind, in the first flow of program its there but not here

- okk give me another test prompt but this time it should actually trigger some of the following criteria didnt have scale, i mean that option

- --pasted debug--
- I mean i did define a scale for salary right? and it wasnt even used

```python
from utils.normalization import normalize_key

def build_explanation_payload(
    results: dict,
    normalized_values: dict,
    raw_values: dict,
    criteria: dict,
    weights: dict
) -> dict:
    """
    Builds a deterministic explanation payload from engine outputs.
    Contains ONLY factual, auditable data.
    """

    ranked_options = list(results.keys())

    # Top user priorities (highest weights)
    user_priorities = sorted(
        weights.keys(),
        key=lambda c: weights[c],
        reverse=True
    )[:3]

    payload = {
        "summary": {},
        "options": {},
        "user_priorities": user_priorities
    }

    # Summary info
    if len(ranked_options) > 1:
        top, second = ranked_options[0], ranked_options[1]
        payload["summary"] = {
            "top_option": top,
            "score_gap_to_next": round(results[top] - results[second], 3)
        }
    else:
        payload["summary"] = {
            "top_option": ranked_options[0],
            "score_gap_to_next": None
        }

    # Per-option explanation
    for rank, option in enumerate(ranked_options, start=1):
        positive = {}
        negative = {}
        missing = []

        for raw_criterion, meta in criteria.items():
            c = normalize_key(raw_criterion)
            if c not in normalized_values.get(option, {}):
                missing.append(raw_criterion)
                continue

            weight = weights.get(raw_criterion, 0)
            ctype = meta["type"]

            contribution = norm_val * weight

            if ctype == "cost":
                negative[raw_criterion] = contribution
            else:
                positive[raw_criterion] = contribution

        payload["options"][option] = {
            "rank": rank,
            "score": results[option],
            "top_positive_factors": sorted(
                positive, key=positive.get, reverse=True
            )[:3],
            "top_negative_factors": sorted(
                negative, key=negative.get, reverse=True
            )[:3],
            "missing_criteria": missing,
            "applied_weights": {
                c: weights[c]
                for c in set(
                    list(positive.keys())[:3] +
                    list(negative.keys())[:3]
                )
            }
        }

    return payload
```
- now norm_val is not defined, i mean all the previous changes does have to work oke?
```text
You defined a scale for 'salary', but no options have salary values.
Would you like to:
[1] Enter salary values now
[2] Continue without salary
```
- if i had to do this would it be a big change?
```python 
6. User confirms ordinal scales
criteria = confirm_ordinal_scales(criteria, options)

# Warn if criteria have no data across all options
for c in criteria:
    if all(
        options.get(opt, {}).get(c) in (None, "unknown")
        for opt in options
    ):
        print(
            f"\nWarning: Some criteria have no data for any option. "
            "Results may be inconclusive."
        )
        break
```
- I just hope this works and doesn't mess with the current flow
- --pasted debug again-- what just happened??
```python
3. User confirms / edits OPTIONS
options = confirm_options(options, criteria)
```
- here?

``` python
explanation_payload = build_explanation_payload(

results=results,

normalized_values=normalized,

raw_values=mapped_attributes,

criteria=criteria,

weights=weights

)
```

- this should be right after results,normalized=compute_weighted_scores() right? in the while True main evaluation loop?

- --pasted debug--
``` python 
Contribution comes from normalized values

norm_val = normalized_values.get(option, {}).get(c)

        if norm_val is None:

            continue



        contributions[raw_criterion] = (

            norm_val * weights.get(raw_criterion, 0)

        )
```
So this in explanation builder should be changed right?
- --pasted debug again--

```text
⚠ You defined a scale for 'work-life balance', but no options have values for it.

Would you like to:

[1] Enter values now

[2] Continue without this criterion

Choice (default = 2):
```
- why the is this asking for this?
```text
⚠ You defined a scale for 'work-life balance', but no options have values for it.

Would you like to:

[1] Enter values now

[2] Continue without this criterion

Choice (default = 2):
```
- TEHHELLLL!!LL!L!L
- WHY IS IT STILL ASKING ME FOR THIS SHIT?? ITS STILL NOT FIXED
-Theres like a quadrillion things just change it and give me the whole thing and also tell me where i should chnge next with the exact file name,i dont wanna guess
- from utils.scale_resolution import resolve_scale_mismatch there's no such thing
- Just give me the fixed code ill just paste
- so basically what did we do? map the ones made by user as user and the automatic ai as ai and it only asks for the humann changed one?
```text
⚠ You defined a scale for 'work-life balance', but no options have values for it.

Would you like to:

[1] Enter values now

[2] Continue without this criterion

Choice (default = 2):
```
- WHYYYYYYYYYYY????1?!!!!
- just modify that and give me the code IM DONE FRRR
- WHERE???? LIKE WHERE SHOW ME LIKE IM BLIND
- --pasted debug again--
- just do it my brain aint braining
- IT WORKED IT WORKEDDD FFSSSSSS
- --pasted debug again--
- we'll do the explanation now
- Okk now that ive got the prompt, i need thw whole thing
```python
import os

import json

from dotenv import load_dotenv

from openai import OpenAI

Load environment variables

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:

raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=API_KEY)

STRUCTURE_SYSTEM_PROMPT = """
```

- this is the starting of my structure agent and i need the explanation agent to use the same open ai
```python
we are going with this, no need to overcompilcate stuff with infra and all.
import os

from dotenv import load_dotenv

from openai import OpenAI

from typing import Dict

import json

Load environment variables

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:

raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=API_KEY)

SYSTEM_PROMPT = """

You are an Explanation Agent for a decision-support system.

Your job is to explain WHY the system ranked options the way it did.

IMPORTANT RULES:

You MUST use ONLY the data provided in the explanation payload.

You MUST NOT introduce new criteria, assumptions, or opinions.

You MUST NOT change rankings, scores, or weights.

You MUST NOT speculate about missing data.

If a criterion is missing or not used, say so clearly.

Be clear, calm, and neutral.

Do not recommend changes unless explicitly asked.


Tone:

clear

Helpful

Honest

Structured

Human-friendly

Non-judgmental


Output format:

1. Short summary (1–2 sentences)


2. Why the top option ranked highest


3. Why other options ranked lower


4. Notes on missing or uncertain information



"""

import os

from dotenv import load_dotenv

from openai import OpenAI

from typing import Dict

import json

Load environment variables

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:

raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=API_KEY)

SYSTEM_PROMPT = """

You are an Explanation Agent for a decision-support system.

Your job is to explain WHY the system ranked options the way it did.

IMPORTANT RULES:

You MUST use ONLY the data provided in the explanation payload.

You MUST NOT introduce new criteria, assumptions, or opinions.

You MUST NOT change rankings, scores, or weights.

You MUST NOT speculate about missing data.

If a criterion is missing or not used, say so clearly.

Be clear, calm, and neutral.

Do not recommend changes unless explicitly asked.


Tone:

Helpful

Honest

Structured

Human-friendly

Non-judgmental


Output format:

1. Short summary (1–2 sentences)


2. Why the top option ranked highest


3. Why other options ranked lower


4. Notes on missing or uncertain information



"""

def render_explanation(

explanation_payload: Dict,

llm_client

) -> str:

"""

Converts a deterministic explanation payload into

a natural language explanation using an LLM.



This function MUST NOT alter payload content.

"""



user_prompt = f"""

Here is the explanation payload from the decision engine:

{json.dumps(explanation_payload, indent=2)}

Explain the ranking to the user.

"""

response = llm_client.generate(

    system_prompt=SYSTEM_PROMPT,

    user_prompt=user_prompt

)



return response.strip()
```
- explanation_payload = build_explanation_payload(...)
where exactly do i add it in main.py note that when user edits the options/criterias.. the explanation shoud be there as well..
- give me a DECISION LENS italic terminal artwork thingy so that once when the main.py is run this decorative text comes, makes it look more polished than bluntly asking "Describe your decison problem" this artwork and then "Describe your decision problem" would look aesthetic and complete

```text
██████╗ ███████╗ ██████╗██╗███████╗██╗ ██████╗ ███╗   ██╗    ██╗     ███████╗███╗   ██╗███████╗

██╔══██╗██╔════╝██╔════╝██║██╔════╝██║██╔═══██╗████╗  ██║    ██║     ██╔════╝████╗  ██║██╔════╝

██║  ██║█████╗  ██║     ██║███████╗██║██║   ██║██╔██╗ ██║    ██║     █████╗  ██╔██╗ ██║███████╗

██║  ██║██╔══╝  ██║     ██║╚════██║██║██║   ██║██║╚██╗██║    ██║     ██╔══╝  ██║╚██╗██║╚════██║

██████╔╝███████╗╚██████╗██║███████║██║╚██████╔╝██║ ╚████║    ███████╗███████╗██║ ╚████║███████║

╚═════╝ ╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝
```

- --pasted debug again--
- tighten the explanation prompt
because the current explanation looks very generic and less simple. dont get me wrong. its detailed but for a normal user it sounds technically

- this is excelent.. holy mother.. I'm done with 90% of the hard part now. Give me a commit msg.
i remember fighting with it in the morning when salary data wasnt available.
implemented the explanation builder and even added explanation agent and lastly did some cleanup
also when does that msg actually pop up? it only comes in certain scenarios the value missing suggestion

- theres this one problem. when i edit the scales and rename it. The current largest scale would ask me where it has to be mapped, if i say ignore and dont map, then all the other renamed scales are not mapped. and when i look at debug , scale is there but it becomes none in mapped

```python
---------- IGNORE ----------

elif choice == "i":

            remaining = unknown_values - ignored - {val}



            if not remaining:

                print(

                    f"\n⚠ WARNING:\n"

                    f"Ignoring this value will leave NO usable data for "

                    f'"{criterion_name}".'

                )

            else:

                print(

                    f"\n⚠ Warning: Ignoring this value will remove "

                    f"usable data for some options under "

                    f'"{criterion_name}".'

                )



            if input("Proceed anyway? (y/n): ").strip().lower() == "y":

                ignored.add(val)

                print(f'\n✔ Ignored "{val}".')

                print_scale(scale)   # ✅ CONFIRM NOTHING ELSE BROKE

                break
```

- just fix this for me

```text

Criterion: ground clearance

Proposed order (worst → best):

1. very low


2. low


3. reasonable


4. high


5. very high



Is this order correct for you? (y/n): n

Enter corrected scale (comma-separated, lowest → highest): low,medium,high

⚠ The following values are not in the scale for 'ground clearance': very_high

You will resolve them one by one.

Resolving value: "very_high"

Choose how to resolve this:

[a] Add to scale

[m] Map to existing value

[i] Ignore this value

[e] Edit entire scale

Choice: i

✔ Ignored "very_high".

⚠ WARNING:

Ignoring this value leaves NO usable data for "ground clearance".

Updated scale (lowest → highest):

1. low


2. medium


3. high



Criteria summary (for ranking):

1. price (cost, unit: lakhs)


2. fuel efficiency (benefit, unit: kmpl)


3. maintenance cost (cost) → scale: very low < low < reasonable < high < very high


4. comfort (benefit) → scale: poor < okay < good < very good < excellent


5. driving feel (benefit) → scale: boring < predictable < decent < good < fun


6. safety (benefit) → scale: poor < average < safe < very safe < excellent


7. ground clearance (benefit) → scale: low < medium < high



Mapped attributes:

Used Toyota Fortuner (2019 diesel): {'price': 32, 'fuel_efficiency': 10, 'maintenance_cost': 4, 'comfort': 5, 'driving_feel': 4, 'safety': 4, 'ground_clearance': None}

New Hyundai Creta (diesel): {'price': 19.5, 'fuel_efficiency': 17, 'maintenance_cost': 3, 'comfort': 3, 'driving_feel': 3, 'safety': 3, 'ground_clearance': None}

Maruti Suzuki Brezza (petrol): {'price': 12, 'fuel_efficiency': 18, 'maintenance_cost': 1, 'comfort': 2, 'driving_feel': 1, 'safety': 2, 'ground_clearance': 1}

Used Skoda Octavia (petrol): {'price': 22, 'fuel_efficiency': 11, 'maintenance_cost': 5, 'comfort': 4, 'driving_feel': 5, 'safety': 5, 'ground_clearance': 1}

New XEV 9e: {'price': 32.0, 'maintenance_cost': 2, 'comfort': 5, 'driving_feel': 5, 'safety': 2, 'ground_clearance': None, 'fuel_efficiency': None}
```

- look i wanted to make the scale small, so i said ignore, there were 5 things in scale and in the new scale there was only 3
```python
# ---------- IGNORE ----------

        elif choice == "i":

            ignored.add(val)

            print(f'✔ Ignored "{val}".')



            if scale_edited:

                print(

                    "ℹ You edited the scale. Ignoring this value may remove data.\n"

                    "Consider mapping it to the nearest value."

                )

                continue  # 🔑 DO NOT finalize yet



            break



            # 🔧 CRITICAL FIX:

            # If scale was edited, we MUST continue resolving others

            if scale_edited:

                print(

                    "ℹ Scale was edited — continuing to resolve remaining values."

                )

                break



            # Old behavior (no edit)

            remaining = unknown_values - ignored

            if not remaining:

                print(

                    f"\n⚠ WARNING:\n"

                    f"Ignoring this value leaves NO usable data for "

                    f'"{criterion_name}".'

                )

            print_scale(scale)

            break
```

- --pasted debug again--

- this is becoming complex and overwhelming atp  jesus christ i havent even started documentation

```python
---------- IGNORE ---------------

elif choice == "i":

            ignored.add(val)

            print(f'✔ Ignored "{val}".')



            if scale_edited:

                print(

                    "ℹ Scale was edited. This value will be auto-compressed "

                    "into the nearest new scale level."

                )

                continue  # DO NOT delete data, keep resolving



            break



            # 🔴 CASE 2: Scale NOT edited → IGNORE is DESTRUCTIVE

            remaining = unknown_values - ignored



            if not remaining:

                print(

                    f"\n⚠ WARNING:\n"

                    f"Ignoring this value leaves NO usable data for "

                    f'"{criterion_name}".'

                )



                if input("Proceed anyway? (y/n): ").strip().lower() != "y":

                    ignored.remove(val)

                    continue



            print_scale(scale)

            break
```
- i replaced the #ignore and ive done only that NOW WHAT???1!!!
- --pasted debug again--
- One critical note (short):
You never persist _previous_scale into criteria before attribute_mapper runs.
So the auto-compress logic I pointed out will only half-work unless:

When a scale is edited (rename/shrink), you do:

Wdym, does this work or not?


-Ill paste the confirm_ordinal_scaes and resolve_scale_mismatch fix it fully for me so that i can copy paste i dont want to play the game of guessing where this goes

- --pasted confirm_ordinal_scales this is the current confirm ordinal scales, i dont want you mess up other things only what is necessary and also comment properly
```python
def resolve_scale_mismatch(

criterion_name: str,

scale: list[str],

unknown_values: set[str]

) -> tuple[list[str], dict[str, str], set[str]]:

"""

Returns:

- updated_scale

- alias_map (e.g. {"mostly_good": "okay"})

- ignored_values

"""



alias_map: dict[str, str] = {}

ignored: set[str] = set()



# 🔧 Track whether scale was edited in THIS function

scale_edited = False



# Helper: suggest mappings by rough semantic similarity

def suggest_mappings(values, scale):

    suggestions = {}

    for v in values:

        v_norm = v.replace("_", " ").lower()

        if "excellent" in v_norm or "extreme" in v_norm:

            suggestions[v] = scale[-1]

        elif "very" in v_norm or "good" in v_norm:

            suggestions[v] = scale[-2] if len(scale) >= 2 else scale[-1]

        elif "okay" in v_norm or "decent" in v_norm:

            suggestions[v] = scale[len(scale) // 2]

        elif "poor" in v_norm or "bad" in v_norm:

            suggestions[v] = scale[0]

    return suggestions



print(

    f"\n⚠ The following values are not in the scale for '{criterion_name}': "

    f"{', '.join(sorted(unknown_values))}"

)

print("You will resolve them one by one.\n")



for val in unknown_values:

    if val in ignored or val in alias_map:

        continue



    print(f'\nResolving value: "{val}"')



    while True:

        choice = input(

            "\nChoose how to resolve this:\n"

            "[a] Add to scale\n"

            "[m] Map to existing value\n"

            "[i] Ignore this value\n"

            "[e] Edit entire scale\n"

            "Choice: "

        ).strip().lower()



        # ---------- ADD ----------

        if choice == "a":

            print_scale(scale)

            pos = input(

                f"Insert '{val}' at position (1–{len(scale)+1}): "

            ).strip()



            if pos.isdigit():

                idx = int(pos) - 1

                if 0 <= idx <= len(scale):

                    scale.insert(idx, val)

                    scale_edited = True

                    print(f'\n✔ Added "{val}" to scale.')

                    print_scale(scale)

                    break



        # ---------- MAP ----------

        elif choice == "m":

            print("\nMap to:")

            for i, s in enumerate(scale, start=1):

                print(f"{i}. {s}")



            sel = input("Choose number: ").strip()

            if sel.isdigit():

                idx = int(sel) - 1

                if 0 <= idx < len(scale):

                    alias_map[val] = scale[idx]

                    print(f'\n✔ Mapped "{val}" → "{scale[idx]}"')

                    print_scale(scale)

                    break

        # ---------- IGNORE ----------

        elif choice == "i":

            # Case 1: Scale WAS edited → IGNORE means compress, not delete

            if scale_edited:

                print(

                    f'✔ "{val}" will be auto-compressed into the nearest '

                    f'scale level after edit.'

                )



                # Mark for auto-mapping later instead of deleting

                alias_map[val] = None  # engine will resolve nearest bucket

                continue  # keep resolving remaining values



            # Case 2: Scale NOT edited → IGNORE is destructive

            remaining = unknown_values - ignored - {val}



            if not remaining:

                print(

                    f"\n⚠ WARNING:\n"

                    f"Ignoring this value leaves NO usable data for "

                    f'"{criterion_name}".'

                )

                if input("Proceed anyway? (y/n): ").strip().lower() != "y":

                    continue



            ignored.add(val)

            print(f'✔ Ignored "{val}".')

            print_scale(scale)

            break



        # ---------- EDIT ENTIRE SCALE ----------

        elif choice == "e":

            new_scale = input(

                "Enter new scale (comma-separated, lowest → highest): "

            ).strip()



            if not new_scale:

                continue



            scale[:] = [s.strip() for s in new_scale.split(",")]

            scale_edited = True

            print(f"\n✔ Replaced entire scale for '{criterion_name}'.")

            print_scale(scale)



            followup = input(

                "\nHandle existing values:\n"

                "[a] Map manually\n"

                "[m] Auto-map similar values\n"

                "[i] Ignore all\n"

                "Choice: "

            ).strip().lower()



            if followup == "m":

                suggestions = suggest_mappings(unknown_values, scale)

                print("\nSuggested mappings:")

                for k, v in suggestions.items():

                    print(f"{k} → {v}")



                if input("Apply these mappings? (y/n): ").strip().lower() == "y":

                    alias_map.update(suggestions)

                    print("\n✔ Auto-mappings applied.")

                    print_scale(scale)

                break



            elif followup == "a":

                for v in unknown_values:

                    print(f"\nMap '{v}' to:")

                    for i, s in enumerate(scale, start=1):

                        print(f"{i}. {s}")

                    sel = input("Choose number (or Enter to skip): ").strip()

                    if sel.isdigit():

                        idx = int(sel) - 1

                        if 0 <= idx < len(scale):

                            alias_map[v] = scale[idx]

                            print(f'✔ Mapped "{v}" → "{scale[idx]}"')

                print_scale(scale)

                break



            elif followup == "i":

                print(

                    f"\n⚠ WARNING: All values ignored for '{criterion_name}'."

                )

                if input("Proceed anyway? (y/n): ").strip().lower() == "y":

                    ignored.update(unknown_values)

                    print_scale(scale)

                break



return scale, alias_map, ignored
```

- thiis is the current resolve_scale_mismatch, dont mess the already working things and only do the fixes. I dont want you to comment the fixes, but only what each block does.

-okk , i want two things to work so thats aliasing and the minimizing of scale, will those two things work? and it should be mapped exactly as well..

```text
Criterion: ground clearance

Proposed order (worst → best):

1. very low


2. low


3. average


4. high


5. very high



Is this order correct for you? (y/n): n

Enter corrected scale (comma-separated, lowest → highest): low,average,high

⚠ You defined a scale for 'ground clearance', but no options have values for it.

Would you like to:

[1] Enter values now

[2] Ignore this criterion

Choice (default = 2): 1

Yeah well crap.. it doesnt let me map it it just goes to the next flow

Enter values for 'ground clearance':

Criteria summary (for ranking):

1. price (cost, unit: lakhs)


2. fuel efficiency (benefit, unit: kmpl)


3. maintenance cost (cost) → scale: very high < high < reasonable < low < very low


4. comfort (benefit) → scale: poor < okay < good < very good < excellent


5. driving feel (benefit) → scale: boring < predictable < decent < good < fun


6. safety (benefit) → scale: poor < average < safe < very safe < excellent


7. ground clearance (benefit) → scale: low < average < high
```
- Ill just go back to last commit
-  --pasted the whole o/p

- how was driving feel ignore? i mean its mapped right? Then why in the explanation payload was it excluded?
```text
Enter corrected scale (comma-separated, lowest → highest): low,average,high

⚠ You defined a scale for 'ground clearance', but no options have values for it.

Would you like to:

[1] Enter values now

[2] Ignore this criterion

Choice (default = 2): 1

Enter values for 'ground clearance':
```
- when this comes over here sometimes it works and takes input from me sometimes it just goes on executing is it detecting an extra enter ?
- where is this part even?
```python
def prompt_missing_values_for_criterion(

criterion: str,

criteria: dict,

options: dict

):

meta = criteria[criterion]

scale = meta.get("scale")

unit = meta.get("unit")



print(f"\nEnter values for '{criterion}':")



for opt in options:

    if options[opt].get(criterion) not in (None, "unknown"):

        continue



    if scale:

        print(f"  {opt} (choose from: {', '.join(scale)}): ", end="")

        val = input().strip()

        options[opt][criterion] = val if val else "unknown"

    else:

        print(f"  {opt} (enter number{f' ({unit})' if unit else ''}): ", end="")

        val = input().strip()

        options[opt][criterion] = float(val) if val else None
```
- just fix it

- --pasted debug again--

- Why isnt driving feel not taken into account, why is it missing? i mean its clearly being mapped
- jesus christ just tell me where all those changes should be done exactly there's like a gazikllion code in here
- great now everything is nuked thank a lot
- im going to the old commit.. thanks a lot dude
- --pasted debug again-- x2
```python
from utils.normalization import normalize_key

def build_explanation_payload(

results: dict,

normalized_values: dict,

raw_values: dict,

criteria: dict,

weights: dict

) -> dict:

"""

Builds a deterministic explanation payload from engine outputs.

Contains ONLY factual, auditable data.

"""



ranked_options = list(results.keys())



# Top user priorities (highest weights)

user_priorities = sorted(

    weights.keys(),

    key=lambda c: weights[c],

    reverse=True

)[:3]



payload = {

    "summary": {},

    "options": {},

    "user_priorities": user_priorities

}



# ---- Summary ----

if len(ranked_options) > 1:

    top = ranked_options[0]

    second = ranked_options[1]

    payload["summary"] = {

        "top_option": top,

        "score_gap_to_next": round(results[top] - results[second], 3)

    }

else:

    payload["summary"] = {

        "top_option": ranked_options[0],

        "score_gap_to_next": None

    }



# ---- Per-option explanation ----

for rank, option in enumerate(ranked_options, start=1):

    positive = {}

    negative = {}

    missing = []



    option_norm_vals = normalized_values.get(option, {})



    for raw_criterion, meta in criteria.items():

        c = normalize_key(raw_criterion)



        # Get normalized value from engine output

        norm_val = option_norm_vals.get(c)



        if norm_val is None:

            missing.append(raw_criterion)

            continue



        # 🔑 IMPORTANT: weights may be keyed by raw OR normalized names

        weight = (

            weights.get(raw_criterion)

            if raw_criterion in weights

            else weights.get(c, 0)

        )



        contribution = norm_val * weight



        if meta["type"] == "cost":

            negative[raw_criterion] = contribution

        else:

            positive[raw_criterion] = contribution



    payload["options"][option] = {

        "rank": rank,

        "score": round(results[option], 3),

        "top_positive_factors": sorted(

            positive,

            key=positive.get,

            reverse=True

        )[:3],

        "top_negative_factors": sorted(

            negative,

            key=negative.get,

            reverse=True

        )[:3],

        "missing_criteria": missing,

        "applied_weights": {

            c: weights[c]

            for c in set(

                list(positive.keys())[:3] +

                list(negative.keys())[:3]

            )

        }

    }



return payload
```
- just fix the whole thing ill paste it
- pasted debug again
- well good news and bad news.. now the explanation builder is getting the data yaay.. bad news is..
- I need help deciding what vehicle to buy, and honestly my thoughts are all over the place.
- i used gemini cli to fix the inconsistancy in data but now...i mean look at it
- --pasted debug again--
```python 
if meta.get("_needs_value_entry"):
from utils.input_helpers import prompt_missing_values_for_criterion
prompt_missing_values_for_criterion(
criterion=raw_key,
criteria=criteria,
options=options
)
meta.pop("_needs_value_entry", None)
```
- where should i even add this? 

```python
def confirm_ordinal_scales(criteria: dict, options: dict) -> dict:

"""

Allows the user to confirm or edit ordinal scales.

Distinguishes between USER-defined and AUTO-generated scales.

"""



# ---------------- helper: auto-generate simple scales ----------------

def auto_generate_scale(criterion_name: str):

    name = criterion_name.lower()



    if "salary" in name or "price" in name:

        return ["low", "medium", "high"]

    if "clearance" in name:

        return ["low", "adequate", "high"]

    if "safety" in name:

        return ["poor", "average", "good"]

    if "comfort" in name:

        return ["poor", "okay", "good", "excellent"]

    if "feel" in name or "driving" in name:

        return ["boring", "decent", "fun"]



    return ["low", "medium", "high"]

# --------------------------------------------------------------------



for raw_key, meta in criteria.items():



    # 🔕 Skip explicitly ignored criteria

    if meta.get("ignored"):

        continue



    key = normalize_key(raw_key)

    scale = meta.get("scale")



    # ---------- detect numeric data ----------

    has_numeric = False

    for opt_vals in options.values():

        val = opt_vals.get(raw_key) or opt_vals.get(key)

        if isinstance(val, (int, float)):

            has_numeric = True

            break

    # ----------------------------------------



    # ---------- scale missing & no numeric ----------

    if not scale and not has_numeric:

        print(f"\nCriterion '{raw_key}' has no numeric values.")

        print("How would you like to handle this?")

        print("[1] Define an ordinal scale (recommended)")

        print("[2] Auto-generate a simple scale for me")

        print("[3] Ignore this criterion")



        choice = input("Choice (default = 1): ").strip() or "1"



        if choice == "1":

            user_scale = input(

                f"Enter ordinal scale for '{raw_key}' "

                "(comma-separated, lowest → highest): "

            ).strip()



            if not user_scale:

                print(f"✔ '{raw_key}' ignored.")

                meta["ignored"] = True

                continue



            meta["scale"] = [s.strip() for s in user_scale.split(",")]

            meta["scale_source"] = "user"

            scale = meta["scale"]



        elif choice == "2":

            auto_scale = auto_generate_scale(raw_key)

            meta["scale"] = auto_scale

            meta["scale_source"] = "auto"

            scale = auto_scale



            print(

                f"✔ Auto-generated scale for '{raw_key}': "

                f"{' < '.join(auto_scale)}"

            )



            # 🔥 NEW: if this was numeric before, allow value entry ONCE

            if has_numeric is False:

                meta["_needs_value_entry"] = True

        else:

            print(f"✔ '{raw_key}' ignored.")

            meta["ignored"] = True

            continue

    # --------------------------------------------



    # Numeric-only criteria → skip

    if not scale:

        continue



    # ---------- confirm scale ----------

    print("\nCriterion:", raw_key)

    print("Proposed order (worst → best):")

    for i, v in enumerate(scale, start=1):

        print(f"{i}. {v}")



    confirm = input("Is this order correct for you? (y/n): ").strip().lower()



    if confirm != "y":

        edited = input(

            "Enter corrected scale (comma-separated, lowest → highest): "

        ).strip()



        if edited:

            meta["scale"] = [s.strip() for s in edited.split(",")]

            meta["scale_source"] = "user"

            scale = meta["scale"]

    # -----------------------------------



    # ---------- detect descriptor mismatches ----------

    detected = set()

    for opt_vals in options.values():

        val = opt_vals.get(key)

        if isinstance(val, str) and normalize_key(val) != "unknown":

            detected.add(normalize_key(val))



    scale_norm = {normalize_key(s) for s in scale}

    missing = detected - scale_norm

    # --------------------------------------------------



    if missing:

        updated_scale, alias_map, ignored_vals = resolve_scale_mismatch(

            criterion_name=raw_key,

            scale=scale,

            unknown_values=missing

        )



        meta["scale"] = updated_scale



        if alias_map:

            meta.setdefault("aliases", {}).update(alias_map)



        if ignored_vals:

            meta.setdefault("ignored_values", set()).update(ignored_vals)

    

            # If this criterion was numeric and got auto-converted to ordinal,

    # allow one explicit value-entry pass

    if meta.get("_needs_value_entry"):

        from utils.input_helpers import prompt_missing_values_for_criterion



        prompt_missing_values_for_criterion(

            criterion=raw_key,

            criteria=criteria,

            options=options

        )



        meta.pop("_needs_value_entry", None)



return criteria
```
- --pasted debug again--
- i mean the engine asked for numeric value , idk numeric values
```python 
elif choice == "3":

criteria = confirm_criteria(criteria, options)

criteria = confirm_criteria_types(criteria)

criteria = confirm_ordinal_scales(criteria, options)



criteria = resolve_empty_scaled_criteria(criteria, options)



criterion_names = list(criteria.keys())

criteria_types = {

    c: meta["type"] for c, meta in criteria.items()

}



mapped_attributes = map_attributes({

    "criteria": criteria,

    "options": options

})
```

- I havent added this in main.py only the confirm_criteria was changed.. shoulld i?

```text
[a] Add criterion  [r] Remove criterion  [c] Continue: a

Enter criterion name: resale value

Is this a benefit or cost? (b = benefit, c = cost): b

Enter unit (or press Enter if not applicable):

ℹ Skipping value entry for 'resale value' — you’ll define a scale next if needed.

Traceback (most recent call last):

File "G:\Decision-Lens\src\main.py", line 265, in <module>

main()

~~~~^^

File "G:\Decision-Lens\src\main.py", line 232, in main

criteria = confirm_criteria(criteria, options)

File "G:\Decision-Lens\src\utils\input_helpers.py", line 436, in confirm_criteria

val = input(prompt).strip()

            ^^^^^^

UnboundLocalError: cannot access local variable 'prompt' where it is not associated with a value

(.venv) PS G:\Decision-Lens\src>
```

```text
ℹ Skipping value entry for 'resale value' — you’ll define a scale next if needed.

Traceback (most recent call last):

File "G:\Decision-Lens\src\main.py", line 265, in <module>

main()

~~~~^^

File "G:\Decision-Lens\src\main.py", line 232, in main

criteria = confirm_criteria(criteria, options)

File "G:\Decision-Lens\src\utils\input_helpers.py", line 435, in confirm_criteria

val = input(prompt).strip()

            ^^^^^^

UnboundLocalError: cannot access local variable 'prompt' where it is not associated with a value

(.venv) PS G:\Decision-Lens\src>
```
- Why is this happening?
```python
def confirm_criteria(criteria: dict, options: dict) -> dict:

"""

Allows the user to add or remove criteria.

If a new criterion is added, immediately asks for values

for all existing options.

"""



while True:

    print("\nIdentified criteria:")

    keys = list(criteria.keys())



    for i, k in enumerate(keys, start=1):

        ctype = criteria[k].get("type", "unknown")

        print(f"{i}. {k} ({ctype})")



    choice = input(

        "\n[a] Add criterion  [r] Remove criterion  [c] Continue: "

    ).strip().lower()



    if choice == "c":

        break



    elif choice == "a":

        name = input("Enter criterion name: ").strip()

        if not name:

            continue



        key = normalize_key(name)



        ctype = input(

            "Is this a benefit or cost? (b = benefit, c = cost): "

        ).strip().lower()



        unit = input(

            "Enter unit (or press Enter if not applicable): "

        ).strip()



        criteria[key] = {

            "type": "benefit" if ctype == "b" else "cost",

            "description": "User-added criterion",

            "scale": [],

            "unit": unit if unit else None

        }



        # NEW PART: ask values for all existing options

        if unit:

            print(f"\nEnter values for new criterion '{name}' (press Enter to skip):")



            for opt, attrs in options.items():

                prompt = f"  {opt} (enter number only, unit: {unit}): "



                while True:

                    val = input(prompt).strip()

                    if not val:

                        break

                    try:

                        attrs[key] = float(val)

                        break

                    except ValueError:

                        print("  Invalid number. Please enter a numeric value.")

        else:

            # No unit → do NOT attempt numeric input

            print(

                f"\nℹ Skipping value entry for '{name}' — "

                "you’ll define a scale next if needed."

            )

            while True:

                val = input(prompt).strip()

                if not val:

                    break



                try:

                    attrs[key] = float(val)

                    break

                except ValueError:

                    print("  Invalid value. Please enter a number only.")



    elif choice == "r":

        idx = input("Enter criterion number to remove: ").strip()

        if idx.isdigit():

            i = int(idx) - 1

            if 0 <= i < len(keys):

                criteria.pop(keys[i])



return criteria
```
```text
ImportError: cannot import name 'confirm_options' from 'utils.input_helpers' (G:\Decision-Lens\src\utils\input_helpers.py)

(.venv) PS G:\Decision-Lens\src> python main.py

Traceback (most recent call last):

File "G:\Decision-Lens\src\main.py", line 7, in <module>

from utils.input_helpers import (

...<9 lines>...

)

ImportError: cannot import name 'confirm_options' from 'utils.input_helpers' (G:\Decision-Lens\src\utils\input_helpers.py)

(.venv) PS G:\Decision-Lens\src>
```
- Im breaking things randomly omg

- Restore or re-add confirm_options
- i cant go back to the last commit dude.. because after fixing the crappy explanation builder i didnt commit ugh..
- i did add all the code above right, so just give me confirm_options

- nvm i looked at the changes and i copy pasted it from there
- yepp,its oficially over i tried many scenarios.. Sooo..yeah Its done couldn't find anything new
- --pasted debug-- it did ask me to rank work life balance, but it didnt let me.. like i didnt even press enter

- yeah well.. im done its working now..

```text
modified:   src/core/__pycache__/attribute_mapper.cpython-313.pyc

    modified:   src/core/__pycache__/decision_engine.cpython-313.pyc

    modified:   src/core/__pycache__/explanation_builder.cpython-313.pyc
```

- should i even include these files in the remote repo?

```text
.venv/

.env

.vscode/

.venv/

.env

.vscode/

Python bytecode

utils/pycache/

*.pyc

*.pyo

*.pyd

core/pycache/

*.pyc

agents/pycache/

*.pyc
```
- those were in all these folders and this is inside gitignore now
```text
(.venv) PS G:\Decision-Lens> git rm --cached -r pycache

fatal: pathspec 'pycache' did not match any files

(.venv) PS G:\Decision-Lens>
```
- I want you to make a architecture diagram with the current files. Also make a simple png file and also a .drawio file so that I can actually make changes if it's wrong

- Next is the data flow diagram. I want you to make a dataflow diagam in the form of png as well as in draw.io format so that i can copy paste into the draw.io

- Yeah.. I dont understand shit just show the dataflow diagram here
- Let's go one by one , I'll draw in a book and lets see if I can make sense out of it.. the more detailed and simplified would be most better
- Where are the input helpers? Where are the ranking?

- --uploaded the drawn image--

- --uploaded the digram-- below is the input_helpers right?
```text
Input Helpers
↓
Attribute Mapper
↓
Decision Engine
↓
Explanation Builder
↓
Explanation Agent
```
- Yeah did all this
- Yeah  this is like primitive  there are no loops and shit
- Just give me the draw.io file With with the correct flow.. so I don't have to fuckn manually draw and waste my Time..make it Clean and human readable make sure there are arrows and markings in there

- Why IS DRAW.IO giving me a miniscule  Image
- WHY IN THE actual f IS THIS THING ZOOMING SOO  IN??
- I JUST WANT THE DIAGRAM AND THIS SHIT ISN'T LETTING ME
- nvm i got it










AI responses were used primarily to:
- Clarify the concept of decision companion systems
- Validate the use of weighted scoring models
- Improve explanation clarity

AI was not used to generate decision logic or rankings.

## Search Queries
- "Weighted decision matrix example"
- "Explainable decision making systems"
- "How to validate weights sum to 1"
- "Data structures for decision making Python"
- "Decision support systems architecture"
- "How to normalize weights so they sum to 1"
- "Python data structures for decision making"
- "Benefit vs cost criteria in decision models"\
- gemini cli windows installation
- what is the role of temperature in AI Agents
- "how do i update all npm packages"
- "how do i open file explorer in windows 11 in that specific path using cmd"
- text to ASCII generator 
- How do i export draw.io files,im only getting a black screren


## References
- Weighted Scoring Model (general decision theory concept)
- Decision Matrix Method
- Basic decision support system design principles
- "https://www.youtube.com/watch?v=J3y1dOpz9R4" was used to for OPEN AI API Key reference
- 
