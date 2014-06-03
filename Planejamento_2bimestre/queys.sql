select count(*),n,mode from execucao group by n,mode;
delete from execucao where id = 1;

.headers on
.mode csv
.output test.csv
select a.nomeAlgoritimo, e.mode,e.n ,avg(d.quantidadeComparacoes),avg(d.quantidadeTrocas),avg(d.tempoExecucao) 
	   from detalhes d
	   join execucao e on e.id = d.execucao_id
	   join algoritimo a on a.id = d.algoritimo_id
	   group by a.nomeAlgoritimo, e.mode, e.n
	   order by e.mode,a.nomeAlgoritimo;
.output stdout
-- Relatório

select a.nomeAlgoritimo, e.mode,e.n ,d.quantidadeComparacoes
	   from detalhes d
	   join execucao e on e.id = d.execucao_id
	   join algoritimo a on a.id = d.algoritimo_id
	   where e.mode = '-A'
	   order by e.mode,a.nomeAlgoritimo;