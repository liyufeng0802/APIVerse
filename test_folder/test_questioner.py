from action_module.questioner import Questioner


def main():
    questioner = Questioner()
    test_input = {
        "curl": "\"curl -X GET https://picsum.photos/{width}/{height}\"",
        "description": " \"Get a random specific size image in specifc width and height\""
    }
    print(questioner.question(test_input["curl"], test_input["description"]))

    '''router = Router()
    response = router.detector("Get me a random joke")
    print(response)'''

if __name__ == "__main__":
    main()