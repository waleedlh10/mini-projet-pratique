const form = document.getElementById("candidate-form");
form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    // 🔥 Transform skills input en JSON string
    const skillsInput = formData.get("skills");
    if (skillsInput) {
        formData.set("skills", JSON.stringify(skillsInput.split(",").map((s) => s.trim())));
    }
    try {
        const response = await fetch("/api/v1/candidates/", {
            method: "POST",
            body: formData,
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.error("Erreur API:", errorData);
            alert("Erreur lors de la création du candidat");
            return;
        }
        alert("Candidat créé avec succès !");
        window.location.href = "/";
    }
    catch (err) {
        console.error("Erreur fetch:", err);
        alert("Erreur lors de la création du candidat");
    }
});
export {};
//# sourceMappingURL=create_candidate.js.map