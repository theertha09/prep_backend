import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class AskDoubtView(APIView):
    def post(self, request):
        question = request.data.get("question", "")
        if not question:
            return Response({"error": "Question is required"}, status=400)

        api_url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer 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",  # replace with your OpenRouter key
            "Referer": "http://localhost",
            "X-Title": "DoubtPadApp"
        }

        payload = {
            "model": "mistralai/mistral-nemo:free",
            "messages": [
                {"role": "user", "content": question}
            ]
        }

        response = requests.post(api_url, headers=headers, json=payload)

        try:
            data = response.json()
            # Remove newline characters
            answer = data["choices"][0]["message"]["content"].replace("\n", " ")
            return Response({"answer": answer})
        except (KeyError, ValueError):
            return Response({
                "error": "Invalid or empty response from OpenRouter",
                "status_code": response.status_code,
                "content": response.text,
            }, status=500)
