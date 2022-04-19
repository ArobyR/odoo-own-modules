# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

log = logging.getLogger(__name__)


class ReportModule(models.Model):
    _name = 'report.module'
    _description = 'Report Module'

    xpath_route = fields.Char(string='Ruta del xpath', default='')
    info_report_id = fields.One2many('info.report', 'report_module_id',
                                     string='Lineas de firmas')
    position = fields.Char(string='Position', default='after')
    views_qweb_id = fields.Many2one(
        'ir.ui.view', domain="[('type', '=', 'qweb')]", string='Vista')

    genered_qweb_view = fields.Many2one('ir.ui.view')

    def unlink(self):
        if self.genered_qweb_view:
            self.genered_qweb_view.unlink()

        return super(ReportModule, self).unlink()

    def create_report(self):
        if self.genered_qweb_view:
            self.genered_qweb_view.unlink()

        description_list = []
        for obj in self.info_report_id:
            description_list.append(obj.description)

        link = self.env['ir.ui.view'].create({"name": f'{self.views_qweb_id.name}01',
                                              "type": self.views_qweb_id.type,
                                              "inherit_id": self.views_qweb_id.id,
                                              "model": self.views_qweb_id.model,
                                              "mode": 'extension',
                                              "priority": self.views_qweb_id.priority,
                                              "key": self.views_qweb_id.key,
                                              "xml_id": self.views_qweb_id.xml_id,
                                              "arch_base": f'''<?xml version="1.0"?>
                                       <data inherit_id="{self.views_qweb_id.xml_id}" priority="{self.views_qweb_id.priority}">
                                       <xpath expr="{self.xpath_route}" position="{self.position}">  
                                        <br/>
                                        <div>
                                          <table style="border:none !important;">
                                            <tr style="border:none !important;">
                                                <span
                                                t-foreach="{description_list}"
                                                t-as="i">
        <td style="border:none !important;padding-right:10px;">___________________________________________</td>
                                                </span>
                                            </tr>
                                            <tr class='text-center' style="border:none !important;">
                                              <span
                                                  t-foreach="{description_list}"
                                                  t-as="i"><td style="border:none 
                                                  !important;"><t t-esc="i"/></td>
                                              </span>
                                            </tr>
                                          </table>
                                        </div>
                                       </xpath>
                                       </data>'''
                                              })
        self.genered_qweb_view = link.id


class InfoReport(models.Model):
    _name = 'info.report'
    _description = 'Informacion del reporte'

    report_module_id = fields.Many2one('report.module')
    description = fields.Char(string='Descripcion:')
