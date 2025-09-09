from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "email", "skills", "cv_url"]

    def validate_skills(self, value):
        """
        Ensure skills is a non-empty list of strings.
        """
        if not isinstance(value, list):
            raise serializers.ValidationError("Skills must be a list.")
        if not all(isinstance(skill, str) for skill in value):
            raise serializers.ValidationError("Each skill must be a string.")
        if not value:
            raise serializers.ValidationError("Skills list cannot be empty.")
        return value

    def validate_cv_url(self, file):
        if file.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("File size must be under 5MB.")
        ext = file.name.split(".")[-1].lower()
        if ext not in ["pdf", "doc", "docx"]:
            raise serializers.ValidationError(
                "Only PDF, DOC, or DOCX files are allowed."
            )
        return file
