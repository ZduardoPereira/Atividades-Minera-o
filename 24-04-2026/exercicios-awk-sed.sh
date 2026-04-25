#!/bin/bash
# Exercicios de manipulacao de textos com AWK e SED
# Arquivo de dados: sensores.csv

FILE="sensores.csv"

echo "=========================================="
echo " EXERCICIO 1"
echo " Separador virgula, imprime ID_Sensor (col3) e Local (col4)"
echo "=========================================="
awk -F',' '{print $3, $4}' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 2"
echo " sed exclui a primeira linha (cabecalho)"
echo "=========================================="
sed '1d' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 3"
echo " awk imprime linhas com Temperatura (col5) > 25.0, ignorando cabecalho"
echo "=========================================="
awk -F',' 'NR > 1 && $5 > 25.0 {print}' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 4"
echo " sed substitui DataCenter por Servidores"
echo "=========================================="
sed 's/DataCenter/Servidores/g' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 5"
echo " awk filtra status OK (col7) e conta total de leituras normais"
echo "=========================================="
awk -F',' '$7 == "OK" {count++} END {print "Total de leituras normais (OK):", count}' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 6"
echo " sed remove todas as linhas que contenham a palavra ERRO"
echo "=========================================="
sed '/ERRO/d' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 7"
echo " awk calcula a media de todas as temperaturas (col5), sem cabecalho"
echo "=========================================="
awk -F',' 'NR > 1 {sum += $5; count++} END {printf "Media de temperatura: %.2f\n", sum/count}' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 8"
echo " sed substitui hifens (-) das datas (col1) por barras (/)"
echo "=========================================="
sed 's/-/\//g' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 9"
echo " awk com array associativo conta envios por sensor (col3)"
echo "=========================================="
awk -F',' 'NR > 1 {contagem[$3]++} END {for (sensor in contagem) print sensor, "->", contagem[sensor], "envios"}' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 10"
echo " sed substitui CRITICO_TEMP por EMERGENCIA, imprimindo apenas linhas alteradas"
echo "=========================================="
sed -n 's/CRITICO_TEMP/EMERGENCIA/gp' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 11"
echo " Pipeline: sed substitui virgulas por espacos, awk imprime col2 e col5"
echo "=========================================="
sed 's/,/ /g' "$FILE" | awk '{print $2, $5}'

echo ""
echo "=========================================="
echo " EXERCICIO 12"
echo " awk encontra a temperatura mais alta (col5)"
echo "=========================================="
awk -F',' 'NR > 1 {if ($5 > max) max = $5} END {print "Temperatura mais alta:", max}' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 13"
echo " sed adiciona [INSPECIONADO] no final das linhas com SNSR-01"
echo "=========================================="
sed '/SNSR-01/s/$/ [INSPECIONADO]/' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 14"
echo " awk com printf: Local (col4) alinhado a esquerda 15 chars + Umidade (col6)"
echo "=========================================="
awk -F',' 'NR > 1 {printf "%-15s %s\n", $4, $6}' "$FILE"

echo ""
echo "=========================================="
echo " EXERCICIO 15"
echo " Pipeline: grep filtra linhas do Armazem, awk soma umidades (col6)"
echo "=========================================="
grep 'Armazem' "$FILE" | awk -F',' '{soma += $6} END {print "Soma total das umidades do Armazem:", soma}'
