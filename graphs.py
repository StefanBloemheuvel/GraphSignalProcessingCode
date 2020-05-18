import networkx as nx

def italy():
	G = nx.Graph()
	G.add_edges_from([("Valle d'Aosta",'Piemonte')])
	G.add_edges_from([("Piemonte","Valle d'Aosta"),('Piemonte','Lombardia'),('Piemonte','Liguria'),('Piemonte','Emilia-Romagna')])
	G.add_edges_from([('Lombardia','P.A. Trento'),('Lombardia','Veneto'),('Lombardia','Emilia-Romagna')])
	G.add_edges_from([('P.A. Trento','Veneto'),('P.A. Trento','Lombardia')])
	G.add_edges_from([('Veneto','P.A. Trento'),('Veneto','Friuli Venezia Giulia'),('Veneto','Emilia-Romagna'),('Veneto','Lombardia')])
	G.add_edges_from([('Emilia-Romagna','Liguria'),('Emilia-Romagna','Lombardia'),('Emilia-Romagna','Toscana'),('Emilia-Romagna','Veneto'),('Emilia-Romagna','Marche'),('Emilia-Romagna','Piemonte')])
	G.add_edges_from([('Liguria','Piemonte'),('Liguria','Emilia-Romagna'),('Liguria','Toscana')])
	G.add_edges_from([('Toscana','Liguria'),('Toscana','Emilia-Romagna'),('Toscana','Umbria'),('Toscana','Lazio'),('Toscana','Marche')])
	G.add_edges_from([('Umbria','Toscana'),('Umbria','Lazio'),('Umbria','Marche')])
	G.add_edges_from([('Marche','Emilia-Romagna'),('Marche','Umbria'),('Marche','Abruzzo'),('Marche','Lazio')])
	G.add_edges_from([('Abruzzo','Marche'),('Abruzzo','Lazio'),('Abruzzo','Molise')])
	G.add_edges_from([('Molise','Abruzzo'),('Molise','Campania'),('Molise','Lazio'),('Molise','Puglia')])
	G.add_edges_from([('Campania','Molise'),('Campania','Lazio'),('Campania','Puglia'),('Campania','Basilicata')])
	G.add_edges_from([('Puglia','Molise'),('Puglia','Campania'),('Puglia','Basilicata')])
	G.add_edges_from([('Basilicata','Puglia'),('Basilicata','Campania'),('Basilicata','Calabria')])
	G.add_edges_from([('Calabria','Basilicata'),('Calabria','Sicilia')])
	G.add_edges_from([('Sicilia','Calabria')])
	
	G.add_edges_from([('P.A. Bolzano','P.A. Trento'),('P.A. Bolzano','Lombardia'),('P.A. Bolzano','Veneto')])
	
	G.remove_node('Sicilia')
	return G