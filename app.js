async function askQuestion() {
    const userInput = document.getElementById("user-input").value;
    const responseDiv = document.getElementById("response");

    const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput }),
    });

    const data = await response.json();
    responseDiv.innerText = data.response || "No response received.";
}

async function uploadFile() {
    const fileInput = document.getElementById("file-input");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData,
    });

    const data = await response.json();
    alert(data.status || data.error);
}
