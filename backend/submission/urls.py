from django.urls import path

from submission.views import SubmissionAPI, ScoreboardAPI, FirstBloodBoardAPI, ChallengeProgressAPI, \
                            ScoreHistoryAPI

urlpatterns = [
    path('submission/', SubmissionAPI.as_view()),
    path('board/score/', ScoreboardAPI.as_view()),
    path('board/firstblood/', FirstBloodBoardAPI.as_view()),
    path('challenge/clear/', ChallengeProgressAPI.as_view()),
    path('board/history/<int:user_id>/', ScoreHistoryAPI.as_view())
]
