from re import S
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
from analizer_pl.C3D.operations import block
from analizer_pl.reports import BnfGrammar
from analizer_pl.abstract import global_env
import analizer_pl.grammar as grammar


def traducir(input):
    result = grammar.parse(input)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    env = global_env.GlobalEnvironment()
    c3d = "from sys import path\n"
    c3d += "from os.path import dirname as dir\n"
    c3d += "path.append(dir(path[0]))\n"
    c3d += "from analizer import interpreter as fase1\n"
    c3d += "from goto import with_goto\n"
    c3d += 'dbtemp = ""\n'
    c3d += "stack = []\n"
    c3d += "\n"
    optimizacion = c3d
    if len(lexerErrors) + len(syntaxErrors) == 0 and result:
        for r in result:
            if r:
                c3d += r.execute(env).value
            else:
                c3d += "Instruccion SQL \n"
    f = open("test-output/c3d.py", "w+")
    f.write(c3d)
    f.close()
    optimizacion += grammar.optimizer_.optimize()
    f = open("test-output/c3dopt.py", "w+")
    f.write(optimizacion)
    f.close()
    semanticErrors = []
    functions = functionsReport(env)
    symbols = symbolReport()
    obj = {
        "lexical": lexerErrors,
        "syntax": syntaxErrors,
        "semantic": semanticErrors,
        "symbols": symbols,
        "functions": functions,
    }
    # grammar.InitTree()
    BnfGrammar.grammarReport()
    return obj


def symbolReport():
    environments = block.environments
    report = []
    for env in environments:
        envName = env[0]
        env = env[1]
        vars = env.variables
        enc = [["ID", "Tipo", "Fila", "Columna", "Declarada en"]]
        filas = []
        for (key, symbol) in vars.items():
            r = [
                symbol.value,
                symbol.type.name if symbol.type else "UNKNOWN",
                symbol.row,
                symbol.column,
                envName,
            ]
            filas.append(r)
        enc.append(filas)
        report.append(enc)
    environments = list()
    return report


def functionsReport(env):
    rep = [["Tipo", "ID", "Tipo de Retorno", "No. de Parametros"], []]
    for (f, x) in env.functions.items():
        r = []
        r.append(x.type)
        r.append(x.id)
        if x.returnType:
            r.append(x.returnType.name)
        else:
            r.append("NULL")
        r.append(x.params)
        rep[1].append(r)
    return rep


s = """ 

CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS integer AS $$
DECLARE 
resultado INTEGER; 
retorna   INTEGER;
BEGIN
	if tabla = 'tbProducto' then
	    resultado := (SELECT md5('23') si, puta as sho) ;
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
	if tabla = 'tbProductoUp' then
	    resultado := (SELECT COUNT(*) FROM tbProducto where estado = 2);
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
	if tabla = 'tbbodega' then
	    resultado := (SELECT COUNT(*) FROM tbbodega);
    	if cantidad = resultado then
			retorna = 1;
		else 
			retorna = 0;
		end if;
	end if;
RETURN retorna;
END;
$$ LANGUAGE plpgsql;
delete from tbbodega as tb where idbodega = 4 and idbodega = 5;
"""
s2 = """

CREATE FUNCTION foo(texto text, b boolean) RETURNS text AS $$
BEGIN
update tbbodega set bodega = texto||"fr", id = 1 where idbodega = 4; 
update tbbodega set bodega = "fr" where idbodega = 4; 
return texto;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION myFuncion(texto text, b boolean) RETURNS text AS $$
BEGIN
INSERT INTO tbProducto values(1,'Laptop Lenovo',md5(texto),1);
SELECT 3-5>4 and -3=texto as sho, texto between symmetric 2 and 3 as alv;

select * from tbCalificacion;
select * from tbventa where ventaregistrada = false;
select * from tbempleadopuesto group by departamento;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;


select v.id+foo(texto, 3)
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido,fechaventa
limit 1;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido
UNION
select DISTINCT * 
from tbventa V,tbempleado E
where V.idempleado = texto
group by 1,2,3
order by 1;

b = texto between symmetric 2 and 3;
RETURN (3+1)*-1;
END;
$$ LANGUAGE plpgsql;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;

select (3+3)*5;

select *
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido
UNION
select DISTINCT * 
from tbventa V,tbempleado E
where V.idempleado = texto
group by 1,2,3
order by col ,1 ;


"""

s3 = """
select E.* from tabla;
select departamento,count(*) CantEmpleados 
from tbempleadopuesto
group by departamento;
select primernombre,segundonombre,primerapellido,sum(montoventa) 
from tbventa V,tbempleado E
where V.idempleado = E.idempleado
group by primernombre,segundonombre,primerapellido;
create table tblibrosalario
( idempleado integer not null,
  aniocalculo integer not null CONSTRAINT aniosalario CHECK (aniocalculo > 0),
  mescalculo  integer not null CONSTRAINT mescalculo CHECK (mescalculo > 0),
  salariobase  money not null,
  comision     decimal,
  primary key(idempleado)
 );
EXECUTE md5("francisco");
update tbbodega set bodega = 'bodega zona 9' where idbodega = 4; 
update tbbodega set bodega = DEFAULT where idbodega = 4; 
"""

s4 = """

CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS integer AS $$
DECLARE resultado INTEGER; 
		retorna   INTEGER;
BEGIN
	if tabla = 'tbProducto' then
	    resultado := not ((4+4*10/3) NOT IN  (SELECT COUNT(*) FROM tbProducto)); 
		retorna = 0;
		
	end if;
	if tabla = 'tbProductoUp' then
	    resultado := xd IN (SELECT * FROM tbProducto where estado = 2);
    	retorna = 1;
	end if;
	if tabla = 'tbbodega' then
	    resultado := EXISTS (SELECT COUNT(*) FROM tbbodega);
    	retorna = 2;
	end if;
RETURN retorna;
END;
$$ LANGUAGE plpgsql;				 
	
"""

traducir(s4)
