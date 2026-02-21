from django.db import models

class Agent(models.Model):
    phone = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Телефон"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    role = models.CharField(
        max_length=20,
        choices=[
            ('agent', 'Агент'),
            ('admin', 'Администратор'),
        ],
        default='agent',
        verbose_name="Роль"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = "Агент"
        verbose_name_plural = "Агенты"


class Deal(models.Model):
    agent = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
        verbose_name="Агент",
        related_name="deals"
    )
    rent_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма аренды (₽)"
    )
    has_insurance = models.BooleanField(
        default=False,
        verbose_name="Страховка оформлена"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата сделки"
    )

    def calculate_commission(self):
        """
        Возвращает словарь с расчётом комиссий
        """
        # Комиссия агента (50% от аренды)
        agent_commission = self.rent_amount * 0.5

        # Наша комиссия (15% от комиссии агента)
        our_commission = agent_commission * 0.15

        # Комиссия со страховки (если есть)
        insurance_commission = 0
        if self.has_insurance:
            # Страховка стоит 10 000, наша доля 25%
            insurance_commission = 10000 * 0.25

        total = our_commission + insurance_commission

        return {
            'agent_commission': round(agent_commission, 2),
            'our_commission': round(our_commission, 2),
            'insurance_commission': round(insurance_commission, 2),
            'total': round(total, 2)
        }

    def __str__(self):
        return f"Сделка {self.id} | {self.agent.name} | {self.rent_amount}₽"

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"