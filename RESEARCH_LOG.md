# Research Log

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
- "1. I need to store the varibles for accepting multiple options.What would be the best data structure? The thing which is coming into my mind is list, as i can store the options as well as criteria and i can  change it in the future as well.."
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
- "ideas are that
- "Idea 1" 

Idea 1
1. **Structure Agent**: Whose only job is to convert user's decision problem into structured data.
2. **Scoring Agent**: Whose job is to estimate relative scores for options against the criteria.
3. **Explanation Agent**: Whose job is to explain decision results clearly and simply.

 Idea 2
1. **Structure Agent (Input → Attributes)** ✅
   - *(AI-assisted, optional)*
   - **What it does:**
     - Takes messy human language
     - Extracts:
       - Options
       - Criteria
       - Cost vs Benefit
       - Raw attributes (numbers, categories, unknowns)

2. **Explanation Agent (Scores → Human Explanation)** 📝
   - *(Optional AI polish)*
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
- "Benefit vs cost criteria in decision models"
- "how do i update all npm packages"
- "how do i open file explorer in windows 11 in that specific path using cmd"



## References
- Weighted Scoring Model (general decision theory concept)
- Decision Matrix Method
- Basic decision support system design principles
- "https://www.youtube.com/watch?v=J3y1dOpz9R4" was used to for OPEN AI API Key reference 
## Accepted vs Rejected Ideas

### Accepted
- Deterministic weighted scoring
- Optional AI-assisted input clarification
- CLI-based initial implementation
- Normalization of weights
- Use of rating scales instead of raw cost values
- Modular Python architecture

### Rejected
- Fully AI-driven decision making
- Chatbot-only interfaces
- Black-box scoring mechanisms
- In the inital phase i had a rating-Based Weighted Sum Mode, that architecture worked mechnically, but it violated my own design principles

