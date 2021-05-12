export default function guardrail(mathFunction) {
    const queue = [];
    const m;
    try {
      m = mathFunction();
    } catch (e) {
      m = e.toString();
    }
    queue.push(m);
    queue.push('Guardrail was processed');
  
    return queue;
}
