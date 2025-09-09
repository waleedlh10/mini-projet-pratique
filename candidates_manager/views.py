from rest_framework import viewsets, mixins
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """
    Candidate API Endpoint

    This API endpoint allows you to manage candidates with the following capabilities:

    Actions:
    - **List Candidates (GET)**: Retrieve a list of all candidates.
      - Supports filtering by skills via the query parameter `skills`.
        Example: `/api/candidates/?skills=python,django`
      - Filters candidates whose skills contain all specified values (case-insensitive).

    - **Create Candidate (POST)**: Add a new candidate.
      - Required fields: `name`, `email`, `skills` (list of strings), `cv_url` (file upload)
      - `skills` can be sent as a JSON array.
      - `cv_url` must be a PDF, DOC, or DOCX file under 5MB.

    Notes:
    - Only **GET** and **POST** methods are allowed; update, delete, or retrieve individual candidates are disabled.
    - File uploads are supported via multipart/form-data.
    """

    http_method_names = ["get", "post"]

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = super().get_queryset()
        skills_param = self.request.query_params.get("skills")
        if skills_param:
            skills_list = [
                skill.strip().lower()
                for skill in skills_param.split(",")
                if skill.strip()
            ]
            for skill in skills_list:
                queryset = queryset.filter(skills__icontains=skill)
        return queryset
