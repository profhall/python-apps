import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from survey_monkey.config import headers

def main():
    surveys_and_responses = get_list_of_surveys()


    print(json.dumps(surveys_and_responses, indent=4))

def get_list_of_surveys():
    """
        returns a list of survey objects with ids & titles

        [
    {
        "title":"Survey 1",
        "id":271052441
        "response_count": 3,
        "questions": []
        },
         {
        "title":"Survey s",
        "id":271062441
        "response_count": 3,
        "questions": []
        },


    ]
    :param headers:
    :return:
    """

    response = requests.get('https://api.surveymonkey.com/v3/surveys',headers=headers, verify=False)
    all_surveys=[]

    for survey in response.json()['data']:
        thisSurvey = {}
        thisSurvey['id'] = survey['id']
        response2 = requests.get(f"https://api.surveymonkey.com/v3/surveys/{survey['id']}/responses", headers=headers, verify=False)
        thisSurvey['title'] = survey['title']
        thisSurvey['responses'] = []
        thisSurvey['response_count'] = response2.json()['total']
        thisSurvey['pages_count'] = None
        thisSurvey['date_modified'] = None
        all_surveys.append(thisSurvey)

    return all_surveys

# def get_survey_responses (surveys):
#     """
#     This will accept a survey id and rerturn the data of that survey
#     GET https://api.surveymonkey.com/v3/surveys/{survey_id}/responses
#
#     :param survey_id:
#     :return:
#     """
#
#     all_surveys ={}
#     # for survey in surveys:
#     #     survey_id = survey['id']
#     response = requests.get(f'https://api.surveymonkey.com/v3/surveys/{271052441}/responses', headers=headers, verify=False)
#         # survey_response = response.json()
#
#         # all_surveys[survey_id] = survey_response
#     # print(json.dumps(all_surveys, indent = 4))
#     print(response.json())
#     return all_surveys

def get_survey_response_data( survey_id, responses):
    all_responses={}

    for res in responses:
        response_id = res['id']
        response = requests.get(f'https://api.surveymonkey.com/v3/surveys/{survey_id}/responses/{response_id}', headers=headers, verify=False)
        all_responses[response_id]= response.json()
    # print(json.dumps(all_responses, indent = 4))

    return all_responses

def get_survey_details(survey_id):
    """
    returns for each survey
    {
     "page_count": 3,
     "category" : "..."
     "last_modification": "",
     "questions":[
        {
            "q_id": 1234,
            "q_text": "..",
            "responses": []
        }
     ]

    }

    :param survey_id:
    :return:
    """

    response = requests.get(f'https://api.surveymonkey.com/v3/surveys/{271052441}/details', headers=headers, verify=False)
    page_count = response.json()["page_count"]
    date_modified = response.json()["date_modified"]
    category = response.json()["category"]
    pages = response.json()["pages"]
    for page in pages:
        description = page["description"]
        for ques in page['questions']:
            q_id = ques['id']
            q_text = ques['headings'][0]['heading']

    print(json.dumps(response.json(), indent = 4))

    return response.json()


if __name__ == '__main__':
    main()
    get_survey_details(4353)






# mockData = [
#     {
#         "title":"Survey 1",
#         "id":271052441
#         "response_count": 3,
#         "questions": {
#             1: {
#                         "id": "..",
#                         "text": "...",
#                         "responses": {
#                             1: {
#                                 "date":"",
#                                 "response": "a response"
#                             },
#                             2: {
#                                 "date":"",
#                                 "response": "a response"
#                             }
#                         }
#                     },
#             2: {
#                         "id": "..",
#                         "text": "...",
#                         "responses": {
#                             1: {
#                                 "date":"",
#                                 "response": "a response"
#                             },
#                             2: {
#                                 "date":"",
#                                 "response": "a response"
#                             }
#                         }
#                     },
#         },
# {
#         "title":"Survey s",
#         "id":272532475
#         "response_count": 3,
#         "questions": {
#             1: {
#                         "id": "..",
#                         "text": "...",
#                         "responses": {
#                             1: {
#                                 "date":"",
#                                 "response": "a response"
#                             },
#                             2: {
#                                 "date":"",
#                                 "response": "a response"
#                             }
#                         }
#                     },
#             2: {
#                         "id": "..",
#                         "text": "...",
#                         "responses": {
#                             1: {
#                                 "date":"",
#                                 "response": "a response"
#                             },
#                             2: {
#                                 "date":"",
#                                 "response": "a response"
#                             }
#                         }
#                     },
#         }
#
#
#
#     ]