from django.core.management.base import BaseCommand
from apps.assessment.models import Article
from apps.assessment.models import Section
from apps.commons.management.data.article_and_sections import blocks_with_sections


class Command(BaseCommand):
    help = 'Creates necessary articles and sections in the database.'

    def handle(self, *args, **kwargs):

        for block in blocks_with_sections:
            article, created = Article.objects.get_or_create(
                code=block['code'],
                defaults={
                    "title": block["title"]
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully created {block["title"]} article'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Article "{block["title"]}" already exists'
                    )
                )

            self.stdout.write("\n")

            for section_data in block['sections']:
                self.create_section(section_data=section_data, article=article)

    def create_section(self, section_data, article: Article):
        section, created = Section.objects.get_or_create(
            title=section_data['title'],
            code=section_data['code'],
            article=article,
            defaults={
                'minimum': section_data['minimum'],
                'maximum': section_data['maximum'],
                'coefficient': section_data['coefficient'],
                'sub_points': section_data['sub_points'],
            }
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created {section_data["title"]} section'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f'Section "{section_data["title"]}" already exists'
                )
            )
