let nextUrl: string | null = null;
let prevUrl: string | null = null;

async function fetchCandidates(url: string = "/api/v1/candidates/") {
  try {
    const response = await fetch(url);
    const data = await response.json();

    const tableBody = document.querySelector(
      "#candidates-table tbody"
    ) as HTMLTableSectionElement;
    tableBody.innerHTML = "";

    data.results.forEach((candidate: any) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${candidate.name}</td>
                <td>${candidate.email}</td>
                <td>${candidate.skills.join(", ")}</td>
                <td><a href="${
                  candidate.cv_url
                }" target="_blank">Voir CV</a></td>
            `;
      tableBody.appendChild(row);
    });

    // Save pagination links
    nextUrl = data.next;
    prevUrl = data.previous;

    // 🔥 Enable/disable buttons depending on API response
    const prevBtn = document.getElementById("prev-btn") as HTMLButtonElement;
    const nextBtn = document.getElementById("next-btn") as HTMLButtonElement;

    prevBtn.disabled = !prevUrl;
    nextBtn.disabled = !nextUrl;
  } catch (error) {
    console.error("Erreur lors du chargement des candidats", error);
  }
}

// Event listeners
document.getElementById("prev-btn")?.addEventListener("click", () => {
  if (prevUrl) fetchCandidates(prevUrl);
});

document.getElementById("next-btn")?.addEventListener("click", () => {
  if (nextUrl) fetchCandidates(nextUrl);
});

// Initial fetch
fetchCandidates();
