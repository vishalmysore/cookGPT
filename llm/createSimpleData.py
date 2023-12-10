from openai import OpenAI
import os

import random
from tenacity import retry, stop_after_attempt, wait_exponential
OPENAI_API_KEY=os.getenv("key")

client = OpenAI(api_key=OPENAI_API_KEY
                )

N_RETRIES = 3

@retry(stop=stop_after_attempt(N_RETRIES), wait=wait_exponential(multiplier=1, min=4, max=70))
def generate_example(temperature=.5):
    messages=[
        {"role" : "system", "content": "You and an OpenAI Fine tuning assistant who can provide me training data in JSONLines format, I need data in the the format i have provided for paneer butter masala"    },
        { "role" : "user", "content": "Give me recipe for Paneer Butter Masala"  },
        { "role": "assistant", "content": "Ingredients:\n\nFor the Paneer Marinade:\n\n250g paneer, cut into cubes\n1/2 cup yogurt\n1 teaspoon ginger-garlic paste\n1/2 teaspoon turmeric powder\n1 teaspoon red chili powder\nSalt to taste\nFor the Gravy:\n\n2 tablespoons butter\n1 tablespoon oil\n1 cup onion, finely chopped\n1 tablespoon ginger-garlic paste\n1 cup tomato puree\n1/2 cup cashew nuts, soaked in water\n1 teaspoon red chili powder (adjust to taste)\n1 teaspoon garam masala\n1 teaspoon coriander powder\n1/2 teaspoon turmeric powder\nSalt to taste\n1 cup water (adjust for desired consistency)\n2 tablespoons fresh cream\n1 teaspoon sugar (optional, to balance the acidity of tomatoes)\nFor Garnish:\n\nFresh coriander leaves, chopped\n1 tablespoon butter (optional)\nInstructions:\n\nMarinate the Paneer:\n\nIn a bowl, mix yogurt, ginger-garlic paste, turmeric powder, red chili powder, and salt.\nAdd paneer cubes to the marinade, ensuring each piece is well-coated.\nAllow it to marinate for at least 30 minutes.\nPrepare the Cashew Paste:\n\nGrind the soaked cashew nuts into a smooth paste using a little water. Set aside.\nCook the Paneer:\n\nHeat 1 tablespoon of butter in a pan and fry the marinated paneer cubes until they turn golden brown. Set aside.\nPrepare the Gravy:\n\nIn the same pan, add 1 tablespoon of oil and another tablespoon of butter.\nAdd chopped onions and sauté until golden brown.\nAdd ginger-garlic paste and sauté for a minute until the raw smell disappears.\nAdd tomato puree and cook until the oil starts to separate from the masala.\nAdd red chili powder, garam masala, coriander powder, turmeric powder, and salt. Cook for a few minutes.\nFinish the Curry:\n\nAdd the cashew paste and mix well.\nPour in water to achieve the desired consistency and bring the curry to a simmer.\nAdd the fried paneer cubes and cook for a few more minutes.\nStir in fresh cream and sugar (if using) to balance the flavors.\nGarnish and Serve:\n\nGarnish with chopped coriander leaves and a dollop of butter.\nServe hot with naan, roti, or rice.\nEnjoy your homemade Paneer Butter Masala"   },
        { "role" : "user", "content": "Give me recipe 3 more indian dishes"  }
    ]




    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
        temperature=temperature,
        max_tokens=1000,
    )
    return response.choices[0].message.content


# Generate examples

example = generate_example()
print(example)