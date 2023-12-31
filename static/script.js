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

document.addEventListener("DOMContentLoaded", function () {
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
  document.getElementById("modal").classList.remove("hidden");
  let data = findBrainPart(title);
  if (data > -1) {
    document.getElementById("modalTitle").innerText = brainParts[data].title;
    document.getElementById("modalTitleInput").value = brainParts[data].title;
    document.getElementById("modalContentInitialize").value =
      brainParts[data].initialize;
    document.getElementById("modalContentPrompt").value =
      brainParts[data].prompt;
    document.getElementById("modalTitle").classList.remove("hidden");
    document.getElementById("modalTitleInput").classList.add("hidden");
  } else {
    document.getElementById("modalTitle").classList.add("hidden");
    document.getElementById("modalTitleInput").classList.remove("hidden");
    document.getElementById("modalTitle").innerText = "";
    document.getElementById("modalTitleInput").value = "";
    document.getElementById("modalContentInitialize").value = "";
    document.getElementById("modalContentPrompt").value = "";
  }
}

function closeModal() {
  document.getElementById("modal").classList.add("hidden");
}

function saveAnswer() {
  let title = document.getElementById("modalTitleInput").value;
  let initialize = document.getElementById("modalContentInitialize").value;
  let promptText = document.getElementById("modalContentPrompt").value;
  localStorage.setItem(title, initialize + "~~" + promptText);

  if (findBrainPart(title) < 0) {
    title = title;
    initialize = initialize;
    promptText = promptText;
    let cardHtml = `
        <div class="mb-4 flex bg-white rounded shadow overflow-hidden" onclick="openModal('${title}', '${initialize.replace(
      /['"]/g,
      " "
    )}', '${promptText.replace(/['"]/g, "'")}')">
            <div class="p-2 flex-grow">
                <h5 class="font-bold text-lg cursor-pointer" >${title}</h5>
                <p class="text-gray-600 text-sm">${initialize}</p>
                <p class="hidden text-gray-600 text-sm">${promptText}</p>
            </div>
        </div>
    `;

    const add = document.getElementById("add");
    add.insertAdjacentHTML("beforebegin", cardHtml);
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
  fetch("/default/brain")
    .then((response) => response.json())
    .then((data) => {
      const sidebar = document.getElementById("sidebar");
      data.forEach((item) => {
        const storedAnswer = localStorage.getItem(item.title);
        let title = item.title;
        let initialize = item.initialize;
        let promptText = item.prompt;
        if (!storedAnswer) {
          localStorage.setItem(
            item.title,
            item.initialize + "~~" + item.prompt
          );
        } else {
          title = item.title;
          parts = storedAnswer.split("~~");
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
        if (item.title == "Add") {
          cardHtml = `
                      <div id="add" class="text-center mb-4 flex bg-white rounded shadow overflow-hidden" onclick="openModal('')">
                          <div class="p-2 flex-grow">
                              <h5 class="font-bold text-lg cursor-pointer" >${title}</h5>
                          </div>
                      </div>
                  `;
        }
        sidebar.insertAdjacentHTML("beforeend", cardHtml);
      });
    });
}

function showAllSpinners() {
  var spinners = document.querySelectorAll(".spinner");
  spinners.forEach(function (spinner) {
    spinner.classList.remove("hidden");
  });
}

function submitChat(event) {
  event.preventDefault(); // Prevent default form submission behavior

  const chatData = {
    situation: document.getElementById("situation").value,
    phenotype: document.getElementById("phenotype").value,
    internalState: document.getElementById("internalState").value,
    motivatedBehavior: document.getElementById("motivatedBehavior").value,
    brainParts: brainParts,
  };

  showAllSpinners();
  fetch("/t1", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(chatData),
  })
    .then((response) => response.json())
    .then((data) => {
      const t2ResponseContainer = document.getElementById("t2Response");
      t2ResponseContainer.innerHTML = "";

      data.forEach((item) => {
        const cardHtml = `
            <div class="border mb-2 p-2">
                <h5 class="font-bold">${item.title}</h5>
                <p>${item.t2.split("-").join("-<br/>")}</p>
                <p>Chat ID: ${item.chat_id}</p>
                <p>Usage: ${item.usage.prompt_tokens}</p>
                <p>Usage: ${item.usage.completion_tokens}</p>
                <p>Usage: ${item.usage.total_tokens}</p>
            </div>
        `;
        t2ResponseContainer.insertAdjacentHTML("beforeend", cardHtml);
        let index = findBrainPart(item.title);
        brainParts[index].chat = item.t2;
      });

      callT4Api(brainParts);
      callT5Api();
      callT6Api();
    });
}

function callT4Api(t3Data) {
  const t4ResponseContainer = document.getElementById("t4Response");

  const chatData = {
    situation: document.getElementById("situation").value,
    phenotype: document.getElementById("phenotype").value,
    internalState: document.getElementById("internalState").value,
    motivatedBehavior: document.getElementById("motivatedBehavior").value,
    brainParts: t3Data,
  };
  fetch("/t4", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(chatData),
  })
    .then((response) => response.json())
    .then((t4Data) => {
      t4ResponseContainer.innerHTML = `
            <div class="border mb-2 p-2">
                <h5 class="font-bold">${t4Data.title}</h5>
                <p>${t4Data.t4.split("-").join("-<br/>")}</p>
                <p>Chat ID: ${t4Data.chat_id}</p>
                <p>Usage: ${t4Data.usage.prompt_tokens}</p>
                <p>Usage: ${t4Data.usage.completion_tokens}</p>
                <p>Usage: ${t4Data.usage.total_tokens}</p>
            </div>
        `;
    });
}

function callT6Api() {
  const t6ResponseContainer = document.getElementById("t6Response");

  const chatData = {
    situation: document.getElementById("situation").value,
    phenotype: document.getElementById("phenotype").value,
    internalState: document.getElementById("internalState").value,
    motivatedBehavior: document.getElementById("motivatedBehavior").value,
  };
  fetch("/t6", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(chatData),
  })
    .then((response) => response.json())
    .then((t6Data) => {
      t6ResponseContainer.innerHTML = `
            <div class="border mb-2 p-2">
                <h5 class="font-bold">${t6Data.title}</h5>
                <p>${t6Data.t6.join("<br/>").split("-").join("-<br/>")}</p>
                <p>Chat ID: ${t6Data.chat_id}</p>
                <p>Usage: ${t6Data.usage.prompt_tokens}</p>
                <p>Usage: ${t6Data.usage.completion_tokens}</p>
                <p>Usage: ${t6Data.usage.total_tokens}</p>
            </div>
        `;
    });
}

function callT5Api() {
  const t5ResponseContainer = document.getElementById("t5Response");

  const chatData = {
    situation: document.getElementById("situation").value,
    phenotype: document.getElementById("phenotype").value,
    internalState: document.getElementById("internalState").value,
    motivatedBehavior: document.getElementById("motivatedBehavior").value,
  };
  fetch("/t5", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(chatData),
  })
    .then((response) => response.json())
    .then((t5Data) => {
      t5ResponseContainer.innerHTML = `
            <div class="border mb-2 p-2">
                <h5 class="font-bold">${t5Data.title}</h5>
                <p>${t5Data.t5b.split("-").join("-<br/>")}</p>
                <br/>
                <p>Brain Parts: ${t5Data.t5.split("-").join("-<br/>")}</p>
                <p>Chat ID: ${t5Data.chat_id}</p>
                <p>Usage: ${t5Data.usage.prompt_tokens}</p>
                <p>Usage: ${t5Data.usage.completion_tokens}</p>
                <p>Usage: ${t5Data.usage.total_tokens}</p>
            </div>
        `;
    });
}
