document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".nav-tab");
    const contents = document.querySelectorAll(".tab-content");

    tabs.forEach(tab => {
        tab.addEventListener("click", function (event) {
            event.preventDefault();

            // Remove 'active' class from all tabs
            tabs.forEach(t => t.classList.remove("active"));
            this.classList.add("active");

            // Hide all tab content
            contents.forEach(content => content.classList.remove("active-content"));

            // Show the content associated with the clicked tab
            const targetId = this.getAttribute("data-tab");
            document.getElementById(targetId).classList.add("active-content");
        });
    });

    
});

