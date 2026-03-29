def get_fallback_rates(weight_kg, origin_pin, dest_pin):
    intra = origin_pin[:3] == dest_pin[:3]
    base = {"DTDC":(40,28,2), "Blue Dart":(55,35,1), "Delhivery":(35,25,3), "India Post":(30,20,4)}
    r = []
    for c,(b,pkg,dy) in base.items():
        cost = b + pkg * weight_kg
        if not intra: cost *= 1.6
        if weight_kg > 10: cost *= 0.9
        r.append({"carrier":c, "rate":round(cost,2), "service":"Surface" if c!="Blue Dart" else "Express", "days":dy if intra else dy+2, "source":"✅ FALLBACK"})
    return sorted(r, key=lambda x:x["rate"])
