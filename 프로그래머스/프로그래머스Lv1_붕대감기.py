
# 붕대감기 1초 -> 체력 += x  연속붕대감기 t초 -> 체력 += y 
# 붕대감기 기술에 공격받으면 기술 연속성공시간무효, 다시 바로 기술시전 
# 공격 당하면 -> 체력 -= 피해량 / 연속성공시간 t==0
# 체력 >= health(최대체력)  
# 체력 <= 0 게임오버
# bandage = [ 연속기술시간, x = 1초당 회복량, y = 추가회복량 ]
# attacks = [[몬스터 공격시간, 피해량], [몬스터 공격시간, 피해량], [몬스터 공격시간, 피해량],.... ]
# 체력<0 -> -1
# 체력>0 -> 체력

#몬스터공격  for attack in attacks : 
# attack_time, damage = attack
# total_time == attack_time 

def health_check(health, max_health):
    if health > max_health:
        return max_health
    return health
    

def solution(bandage, health, attacks):
    max_health = health
    continue_success, x, y = bandage
    total_time, continue_success_time= 1, 0

    for attack in attacks:
        attack_time, damage = attack
        
        while total_time != attack_time:
            continue_success_time += 1
            health += x
            if continue_success_time % continue_success == 0 :
                health += y
            health=health_check(health, max_health)
            total_time += 1
        continue_success_time = 0
        health -= damage
        total_time += 1
        if health <= 0:
            return -1
        
    return health
    
