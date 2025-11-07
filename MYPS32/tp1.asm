# A
.text   # pour dire que la suite c'est du code
main:
    addi $s0, $zero, 0       # a = 0 + 0
    addi $s1, $zero, 1       # b = 0 + 1
    addi $s2, $zero, 2       # c = 0 + 2
    addi $s3, $zero, 3       # d = 0 + 3
    addi $s4, $zero, 4       # e = 0 + 4
    add $t0, $s1, $s2        # t0 = b + c 
    add $t1, $s3, $s4        # t1 = d + e
    sub $s0, $t0, $t1        # a = t0 - t1
    jr $ra                   # fin du premier ex
# B
.text
main2:
    bne $s0, $zero, label1   # if a != 0    # tu appele label comme tu veux genre else
    addi $s1, $s2, 2         # addi car constante, si ya pas de constante genre 2, 4 , 5, alors add
    j end0                   # retour a la ligen end, ici 21
label1:
    add $s3, $s3, $s4        # d = d + e
end0:                         
    jr $ra                   # fin

# C
.text
main3:
    addi $t0, $s0, 1         # création d'une variable temporaire
    slt $t1, $t0, $zero
    beq $t1, $zero, end1
    addi $s0, $s0, -1        # possible avec subi, autoriser a l'exam maiq qtspin veut pas subi
    muli $s1, $s1, 2         # constante donc muli  , instruction facile de mult, mult officiel  #hi, lo, le résultat va dans le registre lo, si surplus de la mult car 32bit, alirs va dans hi
    #multi $s1, 2            #la multiplication "normale"
    #mflo $s1                #pour recup lo et le mettre dans $s1
    j main3                  # retour a main3
end1:
    jr $ra

.text
main4:
    addi $s5, $zero, $zero     #setup a zero e
start:
    addi $s5, $s5, 1            #on rajoute un 
    slti $t0, $s5, 10        #set less than 1 si $s0 < 10
    beq $t0, $zero, end2
    bne $s5, $zero, else1
    add $s0, $zero, $s1
else1:
    add $s0, $s1,$s5
end2:

#version corriger
add $s4, $zero, $zero
FOR : slti $t0, $s4, 10
beq $t0, $zero, EXIT
bne $s4, $zero, ELSE
add $s0, $s1, $zero
j EXIT_IF
ELSE : add $s0, $s1, $s4
EXIT_IF : addi $s4, $s4, 1
j FOR




