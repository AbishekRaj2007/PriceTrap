console.log("🟢 PriceTrap script loaded");

function isProductPage() {
  return (
    window.location.href.includes("/dp/") ||
    window.location.href.includes("/gp/product/")
  );
}

function extractNow() {
  const titleEl = document.getElementById("productTitle");
  const priceEl1 = document.querySelector(".a-price .a-offscreen");
  const priceEl2 = document.querySelector(".a-offscreen");

  console.log("🔎 titleEl:", titleEl);
  console.log("🔎 priceEl1 (.a-price .a-offscreen):", priceEl1);
  console.log("🔎 priceEl2 (.a-offscreen):", priceEl2);

  if (!titleEl) {
    console.log("❌ BLOCKED: productTitle not found");
    return false;
  }

  const priceEl = priceEl1 || priceEl2;
  if (!priceEl) {
    console.log("❌ BLOCKED: price element not found");
    return false;
  }

  const title = titleEl.innerText.trim();
  const rawPrice = priceEl.innerText;

  console.log("🔎 rawPrice text:", rawPrice);

  const priceText = rawPrice.replace(/[₹,]/g, "").trim();
  const price = parseFloat(priceText);

  console.log("🔎 parsed price:", price);

  const productId =
    window.location.pathname.includes("/dp/")
      ? window.location.pathname.split("/dp/")[1]?.split("/")[0]
      : null;

  console.log("🔎 productId:", productId);

  if (!productId || isNaN(price)) {
    console.log("❌ BLOCKED: invalid productId or price");
    return false;
  }

  const product = {
    product_id: productId,
    name: title,
    price: price,
    platform: "amazon"
  };

  console.log("✅ EXTRACTED PRODUCT:", product);

  fetch("http://127.0.0.1:8000/track-price", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(product)
  })
    .then(() => console.log("📤 Sent to backend"))
    .catch(err => console.error("❌ Backend error:", err));

  return true;
}
