let brainParts = [];

function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  var overlay = document.getElementById("overlay");
  sidebar.classList.toggle("-translate-x-full");
  overlay.classList.toggle("hidden");
}

function closeSidebar() {
  var sidebar = document.getElementById("sidebar");
  var overlay = document.getElementById("overlay");
  sidebar.classList.add("-translate-x-full");
  overlay.classList.add("hidden");
}

document.addEventListener('DOMContentLoaded', function () {
  fetchBrainParts();
});

function findBrainPart(title) {
  for (let i = 0; i < brainParts.length; i++) {
    const element = brainParts[i];
    if (title == element.title) {
      return i;
    }
  }
  return -1;
}

function openModal(title) {
  document.getElementById('modal').classList.remove('hidden');
  let data = findBrainPart(title);
  if (data > -1) {
    document.getElementById('modalTitle').innerText = brainParts[data].title;
    document.getElementById('modalTitleInput').value = brainParts[data].title;
    document.getElementById('modalContentInitialize').value = brainParts[data].initialize;
    document.getElementById('modalContentPrompt').value = brainParts[data].prompt;
    document.getElementById('modalTitle').classList.add('hidden');
    document.getElementById('modalTitleInput').classList.remove('hidden');
  } else {
    document.getElementById('modalTitle').classList.remove('hidden');
    document.getElementById('modalTitleInput').classList.add('hidden');
    document.getElementById('modalTitle').innerText = '';
    document.getElementById('modalTitleInput').value = '';
    document.getElementById('modalContentInitialize').value = '';
    document.getElementById('modalContentPrompt').value = '';
  }
}

function closeModal() {
  document.getElementById('modal').classList.add('hidden');
}

function saveAnswer() {
  let title = document.getElementById('modalTitle').innerText;
  let initialize = document.getElementById('modalContentInitialize').value;
  let promptText = document.getElementById('modalContentPrompt').value;
  localStorage.setItem(title, initialize + '~~' + promptText);
  if (findBrainPart(title) < 0) {
    title = title;
    initialize = initialize;
    promptText = promptText;
    let cardHtml = `
        <div class="mb-4 flex bg-white rounded shadow overflow-hidden" onclick="openModal('${title}', '${initialize.replace(/['"]/g, ' ')}', '${promptText.replace(/['"]/g, '\'')}')">
            <div class="p-2 flex-grow">
                <h5 class="font-bold text-lg cursor-pointer" >${title}</h5>
                <p class="text-gray-600 text-sm">${initialize}</p>
                <p class="hidden text-gray-600 text-sm">${promptText}</p>
            </div>
        </div>
    `;
    const add = document.getElementById('add');
    add.insertAdjacentHTML('beforebegin', cardHtml);
    let data = findBrainPart(title);
    if (data > -1) {
      brainParts[data].title = title;
      brainParts[data].initialize = initialize;
      brainParts[data].prompt = promptText;
    } else {
      brainParts.push({ title, initialize, prompt: promptText });
    }
  }
  closeModal();
}

function fetchBrainParts() {
  fetch('/default/brain')
    .then(response => response.json())
    .then(data => {
      const sidebar = document.getElementById('sidebar');
      data.forEach(item => {
        const storedAnswer = localStorage.getItem(item.title);
        let title = item.title;
        let initialize = item.initialize;
        let promptText = item.prompt;
        if (!storedAnswer) {
          localStorage.setItem(item.title, item.initialize + '~~' + item.prompt);
        } else {
          title = item.title;
          parts = storedAnswer.split('~~');
          initialize = parts[0];
          promptText = parts[1];
        }

        brainParts.push({ title, initialize, prompt: promptText });

        let cardHtml = `
                    <div class="mb-4 flex bg-white rounded shadow overflow-hidden" onclick="openModal('${title}')">
                        <div class="p-2 flex-grow">
                            <h5 class="font-bold text-lg cursor-pointer" >${title}</h5>
                            <p class="text-gray-600 text-sm">${initialize}</p>
                            <p class="hidden text-gray-600 text-sm">${promptText}</p>
                        </div>
                    </div>
                `;
        if (item.title == 'Add') {
          cardHtml = `
                      <div id="add" class="text-center mb-4 flex bg-white rounded shadow overflow-hidden" onclick="openModal('')">
                          <div class="p-2 flex-grow">
                              <h5 class="font-bold text-lg cursor-pointer" >${title}</h5>
                          </div>
                      </div>
                  `;
        }
        sidebar.insertAdjacentHTML('beforeend', cardHtml);
      });
    });
}


function submitChat() {
  var chatInput = document.getElementById("chatInput").value;
  fetch("/chat/input", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: chatInput }),
  });
  // Clear the input field
  document.getElementById("chatInput").value = "";
}
