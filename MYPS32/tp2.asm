
# ex 4
.text
main:                         # algo récursif , cas de base et cas récursif
checklist:
    slt $t0, $zero, $a1      #retourne 0 si l est plus grand que zero
    bne $t0, $zero, rec     #va a else si pas egal a zero donc plus petit, sinon reste la  #ici sa marche avec bne et beq mais on pref bne car plus opti
    add $v0, $zero, $zero
    jr $ra
rec:
    addi $a1, $a1, -1
    sll $t0, $t0, 2
    add $t0, $t0, $a1
    lw $t0, 0($t0)
    beq $t0, $a2, if
    addi $sp, $sp, -4
    sw $ra, 0($sp)
    jal checklist
    lw $ra, 0($sp)
    addi $sp, $sp, 4
    jr $ra

if:
    addi $v0, $zero, 1
    jr $ra

# ex5 

.text
main:
# go faire cela en pseudo code python
#on va repartir sur la base de l'ex 4
# def sum_tab(t,l)
    #if l > 0
        #return sum_tab(t,l-1) + t[l-1]
    # else:
        # return 0

#mtn go en mips

.text
main:
sum_tab:
    slt $t0, $zero, $a1
    beq $t0, $zero, else   # va dans le else si plus petit
    addi $a1, $a1, -1  # moins 1 a a valeur
    sll $t0, $a1, 2  # pour calculer le décalage on fait fois 4, on peux aussi faire par mult, fois 4 car chaque élément fait 4 octet
    add $t0, $t0, $a0
    lw $t0, 0($t0)
    addi $sp, $sp, -8
    sw $ra, 0($sp)
    sw $t0, 4($sp)
    jal sum_tab
    lw $ra, 0($sp)
    lw $t0, 4($sp)
    addi $sp, $sp, 8
    add $v0, $v0, $t0
    jr $ra
else:
   add $v0, $zero, $zero #retourne 0
    jr $ra

# ex6
.text
main:
fun:
    beq $a0, $zero, if1  #revoir le choix bne beq
    addi $t0, $zero, 1
    beq $a0, $t0, if2
    addi $a0, $a0, -1
    addi $sp, $sp, -4
    sw $ra, 0($sp)
    jal fun
    sll $v0, $v0, 1
    lw $ra 0($sp)
    addi $sp, $sp, 4
    jr $ra
if2:
    addi $v0, $zero, 2
    jr $ra
if1:
    addi $v0, $zero, 2
    jr $ra
    
