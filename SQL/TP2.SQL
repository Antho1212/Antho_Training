#ex1
Select * from PRODUIT;
#ex2
Select * from PRODUIT where LIBELLE like'%acier%';
#ex3
select distinct LOCALITE from client ;
#ex4
select DISTINCT CAT from CLIENT where LOCALITE like '%Toulouse%';# ou # select DISTINCT CAT from CLIENT where LOCALITE like 'Toulouse'  # ou # select DISTINCT CAT from CLIENT where LOCALITE = '%Toulouse%'
#ex5
select NCLI, Nom, LOCALITE from CLIENT where CAT = 'C1' and LOCALITE <> 'Toulouse'; #ou# select NCLI, Nom, LOCALITE from CLIENT where CAT = 'C1' and not LOCALITE = 'Toulouse' #ou# select NCLI, Nom, LOCALITE from CLIENT where CAT = 'C1' and LOCALITE not in ('Toulouse')
#ex6
select NCLI, Nom, COMPTE from CLIENT where (LOCALITE = 'poitier' or LOCALITE = 'BRUXELLES') and and COMPTE > 0;
#ex7
#a
select NCLI, NOM, LOCALITE, CAT from Client where LOCALITE = 'Lille' or LOCALITE = 'Namur';
#b
select NCLI, NOM, LOCALITE, CAT from CLIENT where LOCALITE = 'Lille' and LOCALITE <> 'Namur';
#c
select NCLI, NOM, LOCALITE, CAT from CLIENT where LOCALITE <> 'Lille' and LOCALITE <> 'Namur';
#d
select NCLI, NOM, LOCALITE, CAT from CLIENT where LOCALITE <> 'Lille' or LOCALITE <> 'Namur';
#e
select NCLI, NOM, LOCALITE, CAT from CLIENT where CAT = 'C1' and LOCALITE = 'Namur';
#f
select NCLI, NOM, LOCALITE, CAT from CLIENT where CAT = 'C1' or LOCALITE <> 'Namur';
#g
select NCLI, NOM, LOCALITE, CAT from CLIENT where CAT = 'C1' and LOCALITE <> 'Namur';
#h
select NCLI, NOM, LOCALITE, CAT from CLIENT where NCLI not in
                                (select NCLI from CLIENT where CAT = 'C1'and LOCALITE <> 'Namur')
#i
select NCLI, NOM, LOCALITE, CAT from CLIENT where (CAT = 'C1'or CAT = 'B1') or (LOCALITE = 'Namur' or LOCALITE = 'Lille');
#j
select NCLI, NOM, LOCALITE, CAT from CLIENT where (CAT in ('C1','B1') and LOCALITE not in ('Lille','Namur')) or (CAT not in ('C1','B1') and LOCALITE in ('Lille','Namur')) ;
#k
select NCLI, NOM, LOCALITE, CAT from CLIENT where (CAT = 'C1'or CAT = 'B1') and (LOCALITE = 'Namur' or LOCALITE = 'Lille');
#l
select NCLI, NOM, LOCALITE, CAT from CLIENT where  not (CAT = 'C1'or CAT = 'B1') and  not (LOCALITE = 'Namur' or LOCALITE = 'Lille');
#ex8
select NCLIn, Nom, LOCALITE from Client Where Nom < LOCALITE
#ex9
select LOCALITE FROM CLIENT where NCLI in (Select NCLI from COMMANDE where NCOM in (select NCOM from DETAIL where NPRO = 'CS464'))
#ex10
select NCLI, NOM from CLIENT where 