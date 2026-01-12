const API_URL = "http://127.0.0.1:8000/query";

export async function queryRag(question: string) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    throw new Error("Failed to fetch from backend");
  }

  return response.json();
}
