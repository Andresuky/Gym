document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los botones con la clase 'dropdown-toggle'
    var dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  
    // Iterar sobre cada botón 'dropdown-toggle'
    dropdownToggles.forEach(function(toggle) {
      toggle.addEventListener('click', function() {
        // Encontrar el siguiente elemento hermano que es el 'dropdown-menu'
        var dropdownMenu = toggle.nextElementSibling;
  
        // Comprobar si el 'dropdown-menu' está visible o no
        var isVisible = dropdownMenu.style.display === 'block';
  
        // Ocultar todos los 'dropdown-menu' antes de mostrar el actual
        hideAllDropdownMenus();
  
        // Mostrar u ocultar el 'dropdown-menu' actual basado en su estado actual
        if (!isVisible) {
          dropdownMenu.style.display = 'block';
        } else {
          dropdownMenu.style.display = 'none';
        }
      });
    });
  
    // Función para ocultar todos los 'dropdown-menu'
    function hideAllDropdownMenus() {
      var allDropdownMenus = document.querySelectorAll('.dropdown-menu');
      allDropdownMenus.forEach(function(menu) {
        menu.style.display = 'none';
      });
    }
  
    // Obtener todos los botones con la clase 'portfolio-btn'
    var portfolioButtons = document.querySelectorAll('.portfolio-btn');
  
    // Iterar sobre cada botón 'portfolio-btn'
    portfolioButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        // Remover la clase 'active' de todos los botones 'portfolio-btn'
        portfolioButtons.forEach(function(btn) {
          btn.classList.remove('active');
        });
  
        // Agregar la clase 'active' solo al botón seleccionado
        button.classList.add('active');
  
        // Obtener el filtro asociado al botón seleccionado
        var filterValue = button.getAttribute('data-filter');
  
        // Aquí puedes usar 'filterValue' para filtrar tu contenido según sea necesario
        console.log('Filtrar por:', filterValue);
  
        // Después de seleccionar un filtro, ocultar todos los 'dropdown-menu'
        hideAllDropdownMenus();
      });
    });
    // Función para mostrar una vista previa de la imagen seleccionada
    function previewImage(event) {
      console.log('Cambio de imagen detectado');
      var reader = new FileReader();
      reader.onload = function() {
        var output = document.getElementById('logo_preview');
        output.src = reader.result;
      };
      reader.readAsDataURL(event.target.files[0]);
    }

    // Reproducir video cuando esté listo para reproducirse
    const video = document.getElementById("video-background");
    video.addEventListener("canplaythrough", function() {
      video.play();
    });
    if (video.readyState >= 3) {
      video.play();
    }
});
