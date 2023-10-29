from questioner import Questioner
from router import Router

def main():
    """questioner = Questioner()
    test_input = {
        "curl": "curl -X GET \"https://api.spaceflightnewsapi.net/v4/articles/{id}/\"",
        "description": "This curl command retrieves a specific article from the Spaceflight News API based on the unique ID provided in the URL. It allows you to access the details of a single article."
    }
    print(questioner.question(test_input["curl"], test_input["description"]))"""

    router = Router()
    response = router.detector("Get me a random joke")
    print(response)

if __name__ == "__main__":
    main()