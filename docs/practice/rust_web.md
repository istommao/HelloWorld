---
title: Rust web实践
order: 12
nav:
  title: Practices
  order: 12
group:
  title: 实战
  order: 1
---


基于 ntex + sea-orm 实现rust web demo

- https://ntex.rs/
- https://github.com/SeaQL/sea-orm

```bash
cargo new rustweb

cd rustweb
```

**编辑Cargo.toml**

```bash
[dependencies]
ntex = { version = "0.7", features = ["tokio"] }
sea-orm = { version = "^0.12.0", features = [ "sqlx-mysql", "runtime-async-std-native-tls", "macros" ] }
```

**编辑 `src/main.rs`**

```rust
use ntex::web;

#[web::get("/")]
async fn hello() -> impl web::Responder {
    web::HttpResponse::Ok().body("Hello world!")
}

#[web::post("/echo")]
async fn echo(req_body: String) -> impl web::Responder {
    web::HttpResponse::Ok().body(req_body)
}

async fn manual_hello() -> impl web::Responder {
    web::HttpResponse::Ok().body("Hey there!")
}

#[ntex::main]
async fn main() -> std::io::Result<()> {
    web::HttpServer::new(|| {
        web::App::new()
            .service(hello)
            .service(echo)
            .route("/hey", web::get().to(manual_hello))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```