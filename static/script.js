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
