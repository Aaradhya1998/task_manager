document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebarBackdrop = document.getElementById("sidebarBackdrop");
    const dashboardLinks = Array.from(
        document.querySelectorAll("[data-dashboard-nav]")
    );
    const dashboardSections = dashboardLinks
        .map((link) => document.querySelector(link.getAttribute("href")))
        .filter(Boolean);

    const closeSidebar = () => {
        sidebar?.classList.remove("show");
        sidebarBackdrop?.classList.remove("show");
    };

    const setActiveDashboardLink = (hash) => {
        dashboardLinks.forEach((link) => {
            link.classList.toggle("active", link.getAttribute("href") === hash);
        });
    };

    sidebarToggle?.addEventListener("click", () => {
        sidebar?.classList.add("show");
        sidebarBackdrop?.classList.add("show");
    });

    sidebarBackdrop?.addEventListener("click", closeSidebar);

    dashboardLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            const target = document.querySelector(link.getAttribute("href"));

            if (target) {
                event.preventDefault();
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
                history.replaceState(null, "", link.getAttribute("href"));
                setActiveDashboardLink(link.getAttribute("href"));
            }

            if (window.innerWidth < 992) {
                closeSidebar();
            }
        });
    });

    if (dashboardSections.length) {
        const sectionObserver = new IntersectionObserver((entries) => {
            const visibleEntry = entries
                .filter((entry) => entry.isIntersecting)
                .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

            if (visibleEntry) {
                setActiveDashboardLink(`#${visibleEntry.target.id}`);
            }
        }, {
            rootMargin: "-20% 0px -55% 0px",
            threshold: [0.15, 0.35, 0.6]
        });

        dashboardSections.forEach((section) => sectionObserver.observe(section));
    }

    document.querySelectorAll(".alert").forEach((alert) => {
        window.setTimeout(() => {
            const instance = bootstrap.Alert.getOrCreateInstance(alert);
            instance.close();
        }, 4500);
    });

    document.querySelectorAll("[data-confirm-delete]").forEach((link) => {
        link.addEventListener("click", (event) => {
            const confirmed = window.confirm("Delete this task?");

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});
const socket = window.io ? io() : null;

const notificationContainer = document.getElementById(
    'liveNotificationContainer'
);

function showNotification(message, type = 'primary') {

    const notification = document.createElement('div');

    notification.className =
        `alert alert-${type} live-notification`;

    notification.innerText = message;

    notificationContainer.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 3000);
}


socket?.on('task_added', (data) => {

    showNotification(
        data.message,
        'success'
    );

    setTimeout(() => {
        location.reload();
    }, 1000);

});


socket?.on('task_updated', (data) => {

    showNotification(
        data.message,
        'warning'
    );

    setTimeout(() => {
        location.reload();
    }, 1000);

});


socket?.on('task_deleted', (data) => {

    showNotification(
        data.message,
        'danger'
    );

    setTimeout(() => {
        location.reload();
    }, 1000);

});
