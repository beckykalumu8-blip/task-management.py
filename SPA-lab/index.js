const searchForm = document.getElementById('search-form');
const wordInput = document.getElementById('word-input');
const resultsDiv = document.getElementById('results');

searchForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const word = wordInput.value.trim().toLowerCase();
    if (!word) return;
    resultsDiv.innerHTML = '<p>Loading...</p>';
    
    try {
        const data = await fetchWordData(word);
        displayResults(data);
    } catch (error) {
        displayError(error.message);
    }
});

async function fetchWordData(word) {
    const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
    if (!response.ok) {
        throw new Error('Word not found or API error. Please try another word.');
    }
    const data = await response.json();
    return data[0];
}

function displayResults(data) {
    resultsDiv.innerHTML = '';

    const wordDiv = document.createElement('div');
    wordDiv.className = 'result-item';
    wordDiv.innerHTML = `<h2>${data.word}</h2><p><strong>Pronunciation:</strong> ${data.phonetic || 'Not available'}</p>`;

    if (data.phonetics && data.phonetics[0] && data.phonetics[0].audio) {
        const audio = document.createElement('audio');
        audio.controls = true;
        audio.src = data.phonetics[0].audio;
        wordDiv.appendChild(audio);
    }
    
    resultsDiv.appendChild(wordDiv);

    data.meanings.forEach(meaning => {
        const meaningDiv = document.createElement('div');
        meaningDiv.className = 'result-item';
        meaningDiv.innerHTML = `<h3>${meaning.partOfSpeech}</h3>`;

        if (meaning.definitions.length > 0) {
            const defList = document.createElement('ul');
            meaning.definitions.forEach(def => {
                const li = document.createElement('li');
                li.textContent = def.definition;
                if (def.example) {
                    li.innerHTML += ` <em>(Example: ${def.example})</em>`;
                }
                defList.appendChild(li);
            });
            meaningDiv.appendChild(defList);
        }

        if (meaning.synonyms && meaning.synonyms.length > 0) {
            const synP = document.createElement('p');
            synP.innerHTML = `<strong>Synonyms:</strong> ${meaning.synonyms.join(', ')}`;
            meaningDiv.appendChild(synP);
        }
        
        resultsDiv.appendChild(meaningDiv);
    });
}

function displayError(message) {
    resultsDiv.innerHTML = `<p class="error">${message}</p>`;
}