<script>
    async function callCohere() {
    try {
    const response = await fetch("https://api.cohere.ai/v1/chat", {
    method: "POST",
    headers: {
    "Authorization": "Bearer TflroiMOXlKaIrEHMr3b71HNTKKBb2Y1uS8Q1S00", // Replace with your actual key
    "Content-Type": "application/json"
},
    body: JSON.stringify({
    model: "command-r7b-12-2024", // Use Cohere's latest "r7b" model
    message: "Give me support resources for independence.",
    max_tokens: 100,
    temperature: 0.7
})
});

    const data = await response.json();
    console.log("Cohere Response:", data);

    // ✅ Output response directly
    if (data.generations && data.generations.length > 0) {
    console.log("AI Response: " + data.generations[0].text);
} else {
    console.log("No response from Cohere.");
}

} catch (error) {
    console.error("Error calling Cohere:", error);
    console.log("Failed to connect to Cohere API.");
}
}

    // Call the function to test
    callCohere();
</script>