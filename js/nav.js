document.addEventListener("DOMContentLoaded", function () {
  // Appeler cette méthode à chaque fois qu'il y a une action scroll.
  window.addEventListener("scroll", function () {
    //Si on scrolle plus 300px (pourquoi 300 ? C'est pour activer cette fonction uniquement qu'on passe le banner (partie hero))
    if (window.scrollY > 300) {
      //Ajouter la class fixed-top dans l'élément qui a le id navbar_top
      document.getElementById("navbar_top").classList.add("fixed-top");
    } else {
      //Sinon on supprime la class fixed-top dans l'élement navbar_top
      document.getElementById("navbar_top").classList.remove("fixed-top");
    }
  });
});
