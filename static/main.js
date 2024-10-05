// static/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Automatisch den Cursor auf das Eingabefeld setzen
    const taskInput = document.querySelector('input[name="task"]');
    if(taskInput) {
        taskInput.focus();
    }
    let taskToDelete = null;

    // Alle "Löschen"-Links holen
    const deleteLinks = document.querySelectorAll('.btn-outline-danger');

    // Modal öffnen, wenn auf "Löschen" geklickt wird
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Verhindert, dass der Link sofort ausgeführt wird
            taskToDelete = this.getAttribute('href'); // Speichert den Link zum Löschen der Aufgabe

            // Das Modal öffnen
            const deleteModal = new bootstrap.Modal(document.getElementById('confirmDeleteModal'));
            deleteModal.show();
        });
    });

    // Wenn der Benutzer im Modal auf 'Löschen' klickt
    const confirmDeleteButton = document.getElementById('confirmDeleteButton');
    confirmDeleteButton.addEventListener('click', function() {
        if (taskToDelete) {
            console.log(taskToDelete); // Debugging: zeigt die zu löschende Aufgabe im Browser-Entwicklung an
            window.location.href = taskToDelete; // Führt die Löschaktion aus
        }
    });
});
