class Brasserie:
    def __init__(self, nom_brasserie, annee_de_creation):
        self.nom_brasserie = nom_brasserie
        self.annee_de_creation = annee_de_creation
        self.styles_biere = []  # Liste des styles de bières produites
        self.fournisseurs = []  # Liste des fournisseurs
        self.vendeurs = []  # Liste des vendeurs

    def est_ouvert(self):
        return True  # Changer le True en False si la brasserie fait faillite

    def ajouter_style_biere(self, style): # Création/mise en production d'un nouveau style de biere
        self.styles_biere.append(style)

    def ajouter_fournisseur(self, fournisseur): # Ajout d'un fournisseur
        self.fournisseurs.append(fournisseur)

    def ajouter_vendeur(self, vendeur): # Ajout d'un vendeur
        self.vendeurs.append(vendeur)


class Fournisseur:
    def __init__(self, nom_fournisseur):
        self.nom_fournisseur = nom_fournisseur
        self.produits_livres = 0

    def qte_produits_livres(self):
        return self.produits_livres # Retourne la quantité totale de produits livrés

class StyleBiere:
    def __init__(self, nom_style):
        self.nom_style = nom_style
        self.bieres = []  # Liste des bières spécifiques associées à ce style

    def nbre_fabriquee(self):
        return sum(biere.quantite_produite for biere in self.bieres) # Retourne le nombre total de bières fabriquées pour ce style

    def ajouter_biere(self, biere):
        self.bieres.append(biere)


class Biere:
    def __init__(self, nom_biere, prix_de_vente, abv):
        self.nom_biere = nom_biere
        self.prix_de_vente = prix_de_vente  # Prix de vente
        self.abv = abv  # Taux d'alcool
        self.quantite_produite = 0

    def produire(self, quantite=1):
        self.quantite_produite += quantite # Ajoute une quantité produite pour cette bière
        print(f"Production de {quantite} unités de la bière {self.nom_biere}")


class Vendeur:
    def __init__(self, nom_vendeur, offre_gratuite):
        self.nom_vendeur = nom_vendeur
        self.offre_gratuite = offre_gratuite  # True si des produits sont offerts gratuitement
        self.produits_commandes = 0

    def nbre_de_produit_commande(self):
        # Retourne le nombre total de produits commandés
        return self.produits_commandes

    def commander(self, quantite):
        # Ajoute une commande de produits
        self.produits_commandes += quantite

# Exemple
def exemple():
    # Création d'une brasserie
    brasserie = Brasserie("Brasserie Ephec", 1995)

    # Ajout d'un fournisseur
    fournisseur = Fournisseur("Fournisseur ABinBEV")
    fournisseur.livrer(100)  # Fournisseur livre 100 unités
    brasserie.ajouter_fournisseur(fournisseur)

    # Ajout d'un style de bière
    style_biere = StyleBiere("Pils")
    brasserie.ajouter_style_biere(style_biere)

    # Ajout d'une bière spécifique à ce style
    biere = Biere("Ephec Pils", 1.2, 5.2)
    biere.produire(50)  # Produire 50 unités de cette bière
    style_biere.ajouter_biere(biere)

    # Ajout d'un vendeur
    vendeur = Vendeur("Beer Bar", offre_gratuite=True)
    vendeur.commander(30)  # Le vendeur commande 30 unités
    brasserie.ajouter_vendeur(vendeur)

    # Appel de méthodes
    print(f"La brasserie {brasserie.nom_brasserie} est ouverte : {brasserie.est_ouvert()}")
    print(f"Style de bière produit : {style_biere.nom_style}")
    print(f"Nombre total de bières fabriquées pour le style {style_biere.nom_style} : {style_biere.nbre_fabriquee()}")
    print(f"Produits livrés par {fournisseur.nom_fournisseur} : {fournisseur.qte_produits_livres()}")
    print(f"Produits commandés par {vendeur.nom_vendeur} : {vendeur.nbre_de_produit_commande()}")

exemple()