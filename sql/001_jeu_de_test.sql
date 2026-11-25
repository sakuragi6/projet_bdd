USE bourse;

DELETE FROM cours WHERE societe_sym IN ('TEST1', 'TEST2');
DELETE FROM bilan WHERE societe_sym IN ('TEST1', 'TEST2');
DELETE FROM societe WHERE symbole IN ('TEST1', 'TEST2');

INSERT INTO societe (symbole, nom, secteur_action, pays) VALUES
  ('TEST1', 'Test Ichi', 'Technologie', 'Japon'),
  ('TEST2', 'Test Ni',  'Energie',     'Tunisie');

INSERT INTO bilan
  (chiffre_affaires, resultat_net, actifs_courants, passifs_courants,
   dettes_totales, capitaux_propres, total_actifs, `date`, societe_sym)
VALUES
  (1000, 50, 150, 100, 300, 600, 900, '2025-12-31', 'TEST1'),
  (2000, 100, 300, 200, 600, 1200, 1800, '2025-12-31', 'TEST2');

INSERT INTO cours (dernier_prix, volume, `date`, societe_sym) VALUES
  (10, 1000, '2025-01-02', 'TEST1'),
  (20, 1100, '2025-01-03', 'TEST1'),
  (30, 1200, '2025-01-04', 'TEST1'),
  (40, 1300, '2025-01-05', 'TEST1'),
  (32, 10000, '2026-01-02', 'TEST2'),
  (46, 11000, '2026-01-03', 'TEST2'),
  (58, 12000, '2026-01-04', 'TEST2'),
  (72, 13000, '2026-01-05', 'TEST1');


