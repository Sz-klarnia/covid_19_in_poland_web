# Opis zmiennych użytych w modelowaniu przebiegu epidemii  
  
W tym pliku można zapoznać się z dokładnym opisem danych, z wykorzystaniem których trenowany był model wykorzystany na stronie.

## Zmienne dotyczące przebiegu epidemii i szczepień

### Źródło: Our World in Data

new_cases_per_million: Nowe wykryte przypadki covid-19 na milion mieszkańców.  
new_deaths_per_million: Nowe zgony spowodowane COVID-19 na milion mieszkańców.  
hosp_patients_per_million: Ilość osób hospitalizowanych z powodu COVID-19 na milion mieszkańców.  
total_vaccinations_per_hundred: Ilość podanych dawek szczepionki na 100 mieszkańców.  
people_vaccinated_per_hundred: Ilość osób, którym podano szczepionkę.  
people_fully_vaccinated_per_hundred: Ilość osób w pełni zaszczepionych (dwiema dawkami bądź szczepionką Johnson & Johnson)  

## Zmienne dotyczące poziomu restrykcji

### Źródło: Government Response Tracker
| ID | Nazwa | Opis | Skala |
| --- | --- | --- | --- |
| C1 | `C1_School closing` | Zamknięcie szkół i  | 0 - Brak restrykcji <br/>1 - Nauczanie hybrydowe <br/>2 - Zamknięcie części szkół (np. liceów i uniwersytetów) <br/>3 - Zamknięcie wszystkich szkół |
| C2 | `C2_Workplace closing` | Zamknięcie miejsc pracy | 0 - Brak restrykcji <br/>1 - Rekomendacja do pracy zdalnej <br/>2 - Nakaz pracy zdalnej dla części sektorów <br/>3 - Zamknięcie wszystkich zakładów oprócz niezbędnych (szpitale, sklepy spożywcze, apteki)|
| C3 | `C3_Cancel public events` | Odwołanie wydarzeń masowych | 0 - Brak restrykcji <br/>1 - Rekomendowane anulowanie wydarzeń <br/>2 - Nakaz anulowania wydarzeń |
| C4 | `C4_Restrictions on gatherings` | Limity zgromadzeń publicznych | 0 - Brak restrykcji <br/>1 - Zakaz zgromadzeń powyżej 1000 osób <br/>2 - Zakaz zgromadzeń powyżej 100 osób <br/>3 - Zakaz zgromadzeń powyżej 10 osób <br/>4 - Pełny zakaz zgromadzeń |
| C5 | `C5_Close public transport` | Ograniczenia w transporcie publicznym | 0 - Brak restrykcji <br/>1 - Ograniczenia rozkładu i dostępności <br/>2 - Zakaz kożystania z transportu zbiorowego |
| C6 | `C6_Stay at home requirements` | Nakaz pozostania w domu | 0 - Brak restrykcji <br/>1 - Rekomendowane pozostanie w domu <br/>2 - Nakaz pozostania w domu oprócz wyjść "niezbędnych" <br/>3 - Zakaz opuszczania domu, ograniczenie możliwości wychodzenia na zakupy itd. |
| C7 | `C7_Restrictions on internal movement` | Restrykcje w przemieszczeniu się po kraju | 0 - Brak restrykcji <br/>1 - Przemieszczanie się po kraju nie rekomendowane <br/>2 - Przemieszczenie się po kraju zakazane |
| C8 | `C8_International travel controls` |  Restrykcje w podróżach zagranicznych | 0 - Brak restrykcji <br/>1 - Notowanie przyjazdów <br/>2 - Kwarantanna dla powracających z części regionów <br/>3 - Zakaz wjazdu z niektórych krajów <br/>4 -Zamknięcie granic |
| H1 | `H1_Public information campaigns` | Kampanie informacyjne | 0 - Brak kampanii <br/>1 - Publiczne wzywanie do zachowania ostrożności <br/>2- Kampanie informacyjne w mediach |
| H2 | `H2_Testing policy` | Dostępność testów |  0 - Brak testowania <br/>1 - Testy dla osób symptomatycznych będących w grupach zagrożenia <br/>2 - Testy dla wszystkich osób z objawami <br/>3 - Otwarte testowanie dla wszystkich chętnych |
| H3 | `H3_Contact tracing` | Śledzenie kontaktów | 0 - Brak śledzenia kontaktów <br/>1 - Ograniczone śledzenie tylko części przypadków <br/>2 - śledzenie wszystkich przypadków |
| H6 | `H6_Facial Coverings` | Maski | 0 - Brak zaleceń <br/>1 - Rekomendowane <br/>2 - Wymagane w części przestrzeni publicznych gdzie ciężko o zachowanie odstępów <br/>3 - Wymagane we wszystkich zamkniętych przestrzeniach  <br/>4 - Wymagane wszędzie poza miejscem zamieszkania |
| H7 | `H7_Vaccination Policy` | Polityka szczepionkowa | 0 - Brak szczepień <br/>1 - Dostępne dla pracowników ochrony zdrowia LUB osób narażonych LUB starszych <br/>2 - Dostępne dla dwóch z trzech grup z poprzedniego punktu <br/>3 - Dostępne dla wszystkich grup z pierwszego punktu <br/>4 - Dostępne także dla innych grup, np. nauczycieli <br/>5 - Dostępne dla wszystkich | 

## Zmienne dotyczące poziomu mobilności społecznej

### Źródło: Google

Zmiana w procentach od poziomu bazowego sprzed epidemii

mobility_parks: Mobilność społeczna w parkach
mobility_retail_and_recreation: Mobilność społeczna w centrach handlowych i miejscach rekreacji
mobility_grocery: Mobilność społeczna związana z codziennymi zakupami
mobility_work: Mobilność społeczna związana z pracą
mobility_transit: MObilność społeczna związana z transportem

## Zmienna dotycząca występowania wariantu brytyjskiego
 
| Nazwa | Skala |
| --- | --- |
| british_strain | 0 - nieobecny <br/> 1 - Do 25% wszystkich przypadków <br/> 2 - Do 50% wszystkich przypadków <br/> 3 - Do 75% przypadków <br/> 4 - Powyżej 75% przypadków |
