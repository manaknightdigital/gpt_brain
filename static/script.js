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

function openModal(title, initialize, promptText) {
  document.getElementById('modal').classList.remove('hidden');
  document.getElementById('modalTitle').innerText = title;
  document.getElementById('modalContentInitialize').value = initialize;
  document.getElementById('modalContentPrompt').value = promptText;
}

function closeModal() {
  document.getElementById('modal').classList.add('hidden');
}

function saveAnswer() {
  const title = document.getElementById('modalTitle').innerText;
  const initialize = document.getElementById('modalContentInitialize').value;
  const promptText = document.getElementById('modalContentPrompt').value;
  localStorage.setItem(title, initialize + ';' + promptText);
  closeModal();
}

function fetchBrainParts() {
  fetch('/default/brain')
    .then(response => response.json())
    .then(data => {
      const sidebar = document.getElementById('sidebar');
      data.forEach(item => {
        const storedAnswer = localStorage.getItem(item.title);
        let title = item.title.replace(/['"]/g, '`');
        let initialize = item.initialize.replace(/['"]/g, '`');
        let promptText = item.prompt.replace(/['"]/g, '`');
        if (!storedAnswer) {
          localStorage.setItem(item.title, item.initialize + ';' + item.prompt);
        } else {
          title = item.title.replace(/['"]/g, '`');
          parts = storedAnswer.split(';');
          initialize = parts[0].replace(/['"]/g, '`');
          promptText = parts[1].replace(/['"]/g, '`');
        }
        const cardHtml = `
                    <div class="mb-4 flex bg-white rounded shadow overflow-hidden" onclick="openModal('${title}', '${initialize}', '${promptText}')">
                        <div class="p-2 flex-grow">
                            <h5 class="font-bold text-lg cursor-pointer" >${title}</h5>
                            <p class="text-gray-600 text-sm">${initialize}</p>
                            <p class="text-gray-600 text-sm">${promptText}</p>
                        </div>
                    </div>
                `;
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
