# 멜로디마켓


## 목표와 기능
1. 목표와 기능
   1. 목표
   2. 기능
   3. 팀구성 - 실제 사진 업로드 
## 개발 환경 및 배포 URL
   1. 기술스택
   2. 개발 환경 (+협업도구)
   3. 배포 URL
   4. URL 구조 (마이크로식)
## 프로젝트 구조
   1. 파일구조    
   2. 브랜치전략
## 아키텍쳐
```mermaid
graph TB
   A[Client] --> B[Lightsail - Frontend Server]
   B --> C[HTML/CSS/JS/Bootstrap]
   B --> D[API Gateway]
   
   D --> E[Lightsail - Backend Server]
   E --> F[Django]
   F --> G[Authentication Service]
   F --> H[Account Service]
   F --> I[Browse Service]
   F --> J[Subscription Service]
   F --> K[Playlist Service]
   F --> L[Review Service]
   
   G --> M[User Database - PostgreSQL]
   H --> M[User Database - PostgreSQL]
   I --> N[Song Database - PostgreSQL]
   J --> O[Subscription Database - PostgreSQL]
   J --> P[Payment Database - PostgreSQL]
   K --> Q[Playlist Database - PostgreSQL]
   L --> R[Review Database - PostgreSQL]

   subgraph Frontend
       C[HTML/CSS/JS/Bootstrap]
   end

   subgraph Backend
       F[Django]
       G[Authentication Service]
       H[Account Service]
       I[Browse Service]
       J[Subscription Service]
       K[Playlist Service]
       L[Review Service]
   end

   subgraph Database
       M[User Database - PostgreSQL]
       N[Song Database - PostgreSQL]
       O[Subscription Database - PostgreSQL]
       P[Payment Database - PostgreSQL]
       Q[Playlist Database - PostgreSQL]
       R[Review Database - PostgreSQL]
   end
```
## 기능 명세 
## 플로우 다이어그램
<img src="https://github.com/melodyteam-org/melodymarket-django/assets/130268717/de1bf85d-d78d-42e3-8697-945b5f25c3f8" width="100%" alt="플로우 다이어그램">

## ERD 다이어그램
```mermaid
erDiagram
    USER ||--o{ GROUP : "belongs to"
    USER ||--o{ PERMISSION : "has"
    USER ||--o{ PLAYLIST : "owns"
    USER ||--o{ SUBSCRIPTION : "subscribes"
    USER ||--|| PAYMENT : "makes"
    USER ||--o{ SONG_REVIEW : "writes"

    GROUP ||--o{ PERMISSION : "grants"

    PLAYLIST ||--o{ PLAYLIST_SONG : "contains"
    SONG ||--o{ PLAYLIST_SONG : "included in"

    SUBSCRIPTION ||--|| PAYMENT : "associated with"

    USER {
        string userID "Unique user ID PK"
        string username "Unique username"
        string email "User email address"
        string password "User password hash"
        string gender "User gender"
        date birthDate "User birth date"
        string provider "Social provider (e.g., Google, Facebook)"
        string accountId "Provider's user ID"
        boolean isSubscribed "User subscription status"
    }

    GROUP {
        string name "Group name"
    }

    PERMISSION {
        string name "Permission name"
    }


    PLAYLIST {
        string id PK
        string userId FK
        string name
        date creationDate
    }

    SONG {
        string id PK
        string title
        string artist
        float duration
    }

    PLAYLIST_SONG {
        string id PK
        string playlistId FK
        string songId FK
    }

    SONG_REVIEW {
        string id PK
        string userId FK
        string songId FK
        string content
        date date
    }

    SUBSCRIPTION {
        string id PK
        string userId FK
        string type
        date startDate
        date endDate
        float price
    }

    PAYMENT {
        string id PK
        string userId FK
        string subscriptionId FK
        float amount
        string status
        date paymentDate
    }
```

## WBS
## 기능명세서
## 와이어프레임
## 역할분담
## 트러블 슈팅
## 개발하며 느낀점 
