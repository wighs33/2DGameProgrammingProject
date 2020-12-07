# 크리처 디펜스 

## 1. 게임소개

이 게임은 워크래프트의 인기 있던 커스텀 게임 중에 하나인 원피스 랜덤 디펜스의 모작입니다.

몬스터가 가장자리를 돌고 유닛으로 몬스터를 최대한 많이 잡아야 합니다.

원피스 랜덤 디펜스 처럼 유닛을 조합할 수 있고 스테이지가 높아질 수록 몬스터의 체력이 증가해서 몬스터를 잡기 어려워지게 됩니다.

![Alt text](https://media.discordapp.net/attachments/374730378738532352/719922277067784293/Warcraft_III_2020-06-09_11_31_23.png?width=814&height=458)

## 2. 게임 조작법

마우스 좌클릭으로 유닛을 이동 시키고 유닛의 사정거리안에 몬스터가 있으면 몬스터를 공격하게 됩니다.

## 3. 게임의 승리 조건

- 스테이지 9를 넘게 되면 게임에서 승리하게 됩니다.

- 몬스터 수가 30을 넘게 되면 게임에서 패배하게 됩니다.

## 4. 게임 플레이

### a. 게임 화면

#### 로딩 화면
![ex_screenshot](./img/loading.png)

  게임을 시작할 때마다 로딩이미지가 랜덤하게 바뀝니다.

#### 타이틀 화면
![ex_screenshot](./img/title.png)
![ex_screenshot](./img/manual.png)

  - 타이틀 음악이 재생됩니다.
  
  - 게임시작 버튼을 누르면 게임플레이 화면으로 넘어 가게 됩니다.
  
  - 게임방법 버튼을 누르면 메모장이 화면에 나타나고 영어로 게임방법에 대해 적혀있습니다.

#### 플레이 화면
![ex_screenshot](./img/gameplay.png)

  - 게임을 플레이 할 수 있습니다.

#### 게임오버 화면
![ex_screenshot](./img/gameover.png)

  - 게임의 승리 조건 혹은 패배 조건을 충족할 시 게임오버 화면 이 나타나게 됩니다.
  
  - 게임에서 승리할 시에 컨티뉴 버튼이 나오는데 컨티뉴 버튼이 나오면 스테이지가 계속해서 증가 하고 몬스터의 체력도 증가하지만 몬스터의 이미지는 바뀌지 않습니다.

### b. 유닛
 ![ex_screenshot](./img/unitfiles/Ace/Idle.png)
  - Ace 
  
 ![ex_screenshot](./img/unitfiles/Akainu/Idle.png)
  - Akainu
  
 ![ex_screenshot](./img/unitfiles/Aokiji/Idle.png)
  - Aokiji 
  
 ![ex_screenshot](./img/unitfiles/BartholomewKuma/Idle.png)
  - Bartholomew Kuma
  
 ![ex_screenshot](./img/unitfiles/Blackbeard/Idle.png)
  - Blackbeard 
  
 ![ex_screenshot](./img/unitfiles/BoaHancock/Idle.png)
  - Boa Hancock 
  
 ![ex_screenshot](./img/unitfiles/Buggy/Idle.png)
  - Buggy
  
 ![ex_screenshot](./img/unitfiles/Chopper/Idle.png)
  - Chopper
  
 ![ex_screenshot](./img/unitfiles/Crocodile/Idle.png)
  - Crocodile 
  
 ![ex_screenshot](./img/unitfiles/DraculeMihawk/Idle.png)
  - Dracule Mihawk
  
 ![ex_screenshot](./img/unitfiles/EmporioIvankov/Idle.png)
  - Emporio Ivankov 
  
 ![ex_screenshot](./img/unitfiles/Jinbei/Idle.png)
  - Jinbei
  
 ![ex_screenshot](./img/unitfiles/Kizaru/Idle.png)
  - Kizaru
  
 ![ex_screenshot](./img/unitfiles/MonkeyDLuffy/Idle.png)
  - MonkeyDLuffy
  
#### 상위 유닛
 ![ex_screenshot](./img/unitfiles/Luffy_lv2/Idle.png)
  - Luffy_lv2
  
 ![ex_screenshot](./img/unitfiles/Shanks_lv2/Idle.png)
  - Shanks_lv2
  

### c. 몬스터
   ![ex_screenshot](./img/monsterfiles/Bulbasaur/Idle.png)
   - stage 1 - Bulbasaur
   
   ![ex_screenshot](./img/monsterfiles/Charmander/Idle.png)
   - stage 2 - Charmander
   
   ![ex_screenshot](./img/monsterfiles/Squirtle/Idle.png)
   - stage 3 - Squirtle
   
   ![ex_screenshot](./img/monsterfiles/Ivysaur/Idle.png)
   - stage 4 - Ivysaur
   
   ![ex_screenshot](./img/monsterfiles/Charmeleon/Idle.png)
   - stage 5 - Charmeleon
   
   ![ex_screenshot](./img/monsterfiles/Wartortle/Idle.png)
   - stage 6 - Wartortle
   
   ![ex_screenshot](./img/monsterfiles/Venusaur/Idle.png)
   - stage 7 - Venusaur
   
   ![ex_screenshot](./img/monsterfiles/Charizard/Idle.png)
   - stage 8 - Charizard
   
   ![ex_screenshot](./img/monsterfiles/Blastoise/Idle.png)
   - stage 9 - Blastoise
   
## 개발 진척도

| 수업주차 | 개발 키워드 | 계획내용 | 개발 내용 |
|---|:---|:---|:---|
| 1주차 | 리소스 | 1. 리소스 수집 <br> 2. 해당 좌표에 리소스 적용 | - 많은 리소스 수집 <br> - 좌표 적용하는데 어려움 겪음
| 2주차 | 유닛 오브젝트 | 1. 유닛 이동과 공격 구현 <br> 2. 이동, 공격애니메이션 구현 <br> 3. 유닛 능력 구현| - 이동, 공격 애니메이션 구현 <br> - 능력은 구현하지 못함
| 3주차 | 건물 오브젝트 | 1. 건물 게이지 구현 <br> 2. 건물 스킬버튼 구현 | -건물 오브젝트는 없는 것이 나을 것 같아서 빼버림
| 4주차 | 몬스터 오브젝트 | 1. 12 스테이지까지 각기 다른 몬스터 이동 공격 구현 <br> 2. 이동, 공격애니메이션 구현 <br> 3. 몬스터 처치시 골드획득 구현 | -9 스테이지까지 각기 다른 몬스터 구현 <br> - 이동애니메이션 구현, 골드는 구현못함
| 5주차 | 조합, 상점 구현 | 1. 조합표, 상점 화면, 버튼 구현 <br> 2. 두 유닛을 조합하여 다른 유닛 생성 구현 | - 랜덤하게 상위유닛으로 조합시키도록 구현 <br> - 상점은 구현하지 못함
| 6주차 | 스테이지, 게임플레이 | 1. 12 스테이지인지 체크, 몬스터 수 50 넘어가면 게임오버 <br> 2. 각각의 게임 상태와 상태 전환 구현| - 9 스테이지가 넘어가면 승리, 몬스터 수30 넘어가면 게임오버 <br> - 몬스터와 유닛이 상호작용하며 상태가 변함
| 7주차 | 사운드 | 1. 사운드 수집 <br> 2. 화면 바뀔 시 다른 음악 적용| - 타이틀 화면음악, 게임오버 시 음악, 메인 게임 음악, 상위 유닛의 목소리 적용
| 8주차 | 점검, 수정 | 1. 최종 점검, 오류 수정 <br> 2. 릴리즈하기 | - 릴리즈 완료
| 9주차 | 발표 | 1. 발표준비 |
