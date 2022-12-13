from app import extract_comments

url = "https://www.reddit.com/r/europe/comments/r0hthg/sweden_is_taking_the_lead_to_persuade_the_rest_of/"

def test_classifier(input_url = url):
    return extract_comments(input_url)
