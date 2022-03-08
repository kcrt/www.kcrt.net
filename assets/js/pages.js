
document.addEventListener('DOMContentLoaded', () => {

    /* ===== Handle Humberger Menu (bulma) ===== */
    // Get all "navbar-burger" elements
    const navbarBurger = document.querySelector(".navbar-burger");
    navbarBurger.addEventListener("click", (event) => {
        // Get the target from the "data-target" attribute
        const $target = event.target
        const $menu = document.getElementById($target.dataset.target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $menu.classList.toggle('is-active');
        $target.classList.toggle('is-active');

    });
  
    /* ===== Notification close box ===== */
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
        const $notification = $delete.parentNode;
        $delete.addEventListener('click', () => {
            $notification.parentNode.removeChild($notification);
        });
    });

    /* ===== Add 'table' class to all tables ===== */
    const tables = document.querySelectorAll("table");
    for (const table of tables){
        table.classList.add("table", "is-bordered");
    }

    /* ===== domain check ===== */
    const domain = document.domain;
    switch(domain){
        case "localhost":
            document.getElementById("navbar").classList.add("tiger")
            break;
        case "kcrt.github.io":
            document.getElementById("content").classList.add("blur")
    }

});