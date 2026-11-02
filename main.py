from dataclasses import dataclass
from typing import List

@dataclass
class Offer:
    provider: str
    model: str
    input_per_m: float
    output_per_m: float

OFFERS = [
    Offer('ProviderA', 'gpt-mini', 0.15, 0.60),
    Offer('ProviderB', 'gpt-mini', 0.10, 0.50),
    Offer('ProviderC', 'gpt-mini', 0.12, 0.55),
    Offer('ProviderA', 'llama-3', 0.05, 0.10),
    Offer('ProviderB', 'llama-3', 0.04, 0.12),
]

def cost(offer: Offer, input_tokens: int, output_tokens: int) -> float:
    return (input_tokens / 1_000_000) * offer.input_per_m + (output_tokens / 1_000_000) * offer.output_per_m

def find_cheapest(model: str, input_tokens: int = 1000, output_tokens: int = 500) -> List[Offer]:
    candidates = [o for o in OFFERS if o.model == model]
    return sorted(candidates, key=lambda o: cost(o, input_tokens, output_tokens))

def main():
    model = 'gpt-mini'
    input_tokens = 10000
    output_tokens = 2000
    print(f'Cheapest API offers for {model}:')
    for i, offer in enumerate(find_cheapest(model, input_tokens, output_tokens), 1):
        total = cost(offer, input_tokens, output_tokens)
        print(f'{i}. {offer.provider}: ${total:.6f} (in ${offer.input_per_m}/M, out ${offer.output_per_m}/M)')

if __name__ == '__main__':
    main()