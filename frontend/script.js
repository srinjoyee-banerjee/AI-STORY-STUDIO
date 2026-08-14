
const generateBtn = document.getElementById("generateBtn");

const storyOutput = document.getElementById("storyOutput");
const loading = document.getElementById("loading");


// ============================================================
// GENERATE STORY
// ============================================================

generateBtn.addEventListener("click", async () => {

    const idea = document.getElementById("idea").value.trim();
    const genre = document.getElementById("genre").value;
    const tone = document.getElementById("tone").value;


    // Validate input
    if (!idea) {

        alert("Please enter a story idea.");

        return;
    }


    // Loading state
    loading.classList.remove("hidden");

    storyOutput.innerHTML = `
        <p>✨ Creating your story...</p>
    `;

    generateBtn.disabled = true;


    try {

        const response = await fetch(
            "/api/generate-story",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    idea: idea,
                    genre: genre,
                    tone: tone
                })
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.message || "Story generation failed."
            );
        }


        // Display generated story
        storyOutput.innerHTML = `
            <h3>${data.title}</h3>
            <br>
            <div class="story-text">
                ${formatStory(data.story)}
            </div>
        `;


    } catch (error) {

        console.error(error);

        storyOutput.innerHTML = `
            <p>
                ❌ ${error.message}
            </p>
        `;

    } finally {

        loading.classList.add("hidden");

        generateBtn.disabled = false;
    }

});


// ============================================================
// FORMAT STORY
// ============================================================

function formatStory(text) {

    return text
        .replace(/\n\n/g, "<br><br>")
        .replace(/\n/g, "<br>");
}
