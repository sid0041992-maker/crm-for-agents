from django.db import models

class User(models.Model):
    ROLES = [
        ('agent', 'Агент'),
        ('owner', 'Собственник'),
        ('tenant', 'Арендатор'),
    ]
    phone = models.CharField(max_length=15, unique=True, verbose_name="Телефон")
    name = models.CharField(max_length=100, verbose_name="Имя")
    role = models.CharField(max_length=20, choices=ROLES, default='agent', verbose_name="Роль")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile', verbose_name="Пользователь")

    def __str__(self):
        return f"Агент: {self.user.name}"

    class Meta:
        verbose_name = "Агент"
        verbose_name_plural = "Агенты"


class Property(models.Model):
    PROPERTY_TYPES = [
        ('flat', 'Квартира'),
        ('house', 'Дом'),
        ('studio', 'Студия'),
        ('commercial', 'Коммерческое'),
    ]
    STATUSES = [
        ('active', 'Активен'),
        ('archived', 'В архиве'),
        ('rented', 'Сдан'),
    ]

    address = models.CharField(max_length=255, verbose_name="Адрес")
    area = models.DecimalField(max_digits=6, decimal_places=1, verbose_name="Площадь (м²)")
    floor = models.IntegerField(verbose_name="Этаж")
    total_floors = models.IntegerField(verbose_name="Всего этажей")
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, verbose_name="Тип")
    status = models.CharField(max_length=20, choices=STATUSES, default='active', verbose_name="Статус")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_properties')
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agent_properties')

    main_image = models.URLField(blank=True, verbose_name="Главное фото")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class Deal(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name="Агент", related_name="deals")
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма аренды (₽)")
    has_insurance = models.BooleanField(default=False, verbose_name="Страховка оформлена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата сделки")

    def calculate_commission(self):
        agent_commission = self.rent_amount * 0.5
        our_commission = agent_commission * 0.15
        insurance_commission = 0
        if self.has_insurance:
            insurance_commission = 10000 * 0.25
        total = our_commission + insurance_commission
        return {
            'agent_commission': round(agent_commission, 2),
            'our_commission': round(our_commission, 2),
            'insurance_commission': round(insurance_commission, 2),
            'total': round(total, 2)
        }

    def __str__(self):
        return f"Сделка {self.id} | {self.agent.user.name} | {self.rent_amount}₽"

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"