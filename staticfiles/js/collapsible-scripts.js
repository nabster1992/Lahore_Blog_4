document.addEventListener('DOMContentLoaded', function () {
  bulmaCollapsible.attach('.is-collapsible');

  // Get all collapsible elements
  var collapsibles = document.querySelectorAll('.is-collapsible');

  // Attach click event to each collapsible element
  collapsibles.forEach(function (collapsible) {
      var toggleButton = collapsible.querySelector('[data-action="collapse"]');

      toggleButton.addEventListener('click', function (event) {
          event.preventDefault();

          // Close all other collapsibles except the one being clicked
          collapsibles.forEach(function (otherCollapsible) {
              if (otherCollapsible !== collapsible) {
                  otherCollapsible.classList.add('is-collapsed');
              }
          });

          // Toggle the visibility of the clicked collapsible element
          collapsible.classList.toggle('is-collapsed');
      });
  });
});



